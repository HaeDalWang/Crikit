#!/usr/bin/env python3
"""
Verify that a URL is reachable and returns a valid response.
Used by criki to validate documentation links before citing them.

Strategy:
    1. Try HEAD first (lightweight)
    2. If HEAD fails (405, 403, etc.), fallback to GET with range header
    This handles sites like AWS docs, HashiCorp docs that block HEAD requests.

Usage:
    python verify_url.py <url>

Exit codes:
    0 — URL is reachable
    1 — URL is unreachable or returned an error
"""

import sys
import urllib.request
import urllib.error

USER_AGENT = "criki-evidence-grounding/1.0"
TIMEOUT = 10


def try_head(url: str) -> bool:
    req = urllib.request.Request(url, method="HEAD")
    req.add_header("User-Agent", USER_AGENT)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.status == 200


def try_get(url: str) -> bool:
    req = urllib.request.Request(url, method="GET")
    req.add_header("User-Agent", USER_AGENT)
    req.add_header("Range", "bytes=0-1024")
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.status in (200, 206)


def verify(url: str) -> bool:
    for method in (try_head, try_get):
        try:
            if method(url):
                return True
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
            continue
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
