from scholarly import ProxyGenerator, scholarly
import json
from datetime import datetime
import os
import time


def _enable_proxy() -> None:
    # FreeProxies helps reduce failures on GitHub-hosted runners.
    pg = ProxyGenerator()
    if pg.FreeProxies():
        scholarly.use_proxy(pg)


def _fetch_author(author_id: str, retries: int = 3) -> dict:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            author: dict = scholarly.search_author_id(author_id)
            scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
            return author
        except Exception as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(4 * attempt)
    raise RuntimeError(f"Failed to fetch Google Scholar profile {author_id}: {last_error}")


def _write_results(author: dict, error: str | None = None) -> None:
    author["updated"] = datetime.now().isoformat()
    if isinstance(author.get("publications"), list):
        author["publications"] = {
            p.get("author_pub_id", f"pub_{idx}"): p
            for idx, p in enumerate(author["publications"])
            if isinstance(p, dict)
        }
    if error:
        author["error"] = error

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 'N/A')}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


def main() -> int:
    author_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not author_id:
        raise RuntimeError("Missing GOOGLE_SCHOLAR_ID environment variable.")

    _enable_proxy()
    fail_on_error = os.environ.get("FAIL_ON_FETCH_ERROR", "0") == "1"

    try:
        author = _fetch_author(author_id)
        _write_results(author)
        print(json.dumps(author, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(f"Warning: {exc}")
        _write_results({"scholar_id": author_id}, error=str(exc))
        return 1 if fail_on_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
