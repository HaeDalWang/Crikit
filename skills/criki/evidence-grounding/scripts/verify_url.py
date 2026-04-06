#!/usr/bin/env python3
"""
Verify that a URL is reachable and returns a valid response.
Used by criki to validate documentation links before citing them.

Usage:
    python verify_url.py <url>

Exit codes:
    0 — URL is reachable (HTTP 200)
    1 — URL is unreachable or returned an error
"""

import sys
import urllib.request
import urllib.error


def verify(url: str) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD")
        req.add_header("User-Agent", "criki-evidence-grounding/1.0")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_url.py <url>")
        sys.exit(1)

    target = sys.argv[1]
    if verify(target):
        print(f"OK: {target}")
        sys.exit(0)
    else:
        print(f"FAIL: {target} is unreachable or returned an error")
        sys.exit(1)
