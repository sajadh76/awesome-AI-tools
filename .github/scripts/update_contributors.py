"""Rebuild the contributors grid in README.md.

Lists the repository's contributors from the GitHub API and leaves out:
- bot accounts,
- usernames in .github/contributors-blocklist.txt,
- accounts that still have GitHub's default pattern avatar (an "identicon").

The grid is written between the contributors:start and contributors:end markers.
"""
import io
import json
import os
import re
import sys
import urllib.request

from PIL import Image

REPO = os.environ.get("GITHUB_REPOSITORY", "sajadh76/awesome-AI-tools")
TOKEN = os.environ.get("GITHUB_TOKEN")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
README = os.path.join(ROOT, "README.md")
BLOCKLIST = os.path.join(ROOT, ".github", "contributors-blocklist.txt")
START, END = "<!-- contributors:start -->", "<!-- contributors:end -->"
PER_ROW = 12
SIZE = 64


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "contributors-grid"})
    if TOKEN and url.startswith("https://api.github.com/"):
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def contributors():
    page, out = 1, []
    while True:
        batch = json.loads(get(f"https://api.github.com/repos/{REPO}/contributors?per_page=100&page={page}"))
        if not batch:
            return out
        out += batch
        page += 1


def has_default_avatar(avatar_url):
    # GitHub's default avatar is a 5x5 pattern in one colour on a #F0F0F0 background.
    img = Image.open(io.BytesIO(get(avatar_url))).convert("RGB")
    colours = img.getcolors(16)
    return colours is not None and len(colours) <= 2 and any(c == (240, 240, 240) for _, c in colours)


def main():
    blocked = set()
    if os.path.exists(BLOCKLIST):
        for line in open(BLOCKLIST, encoding="utf-8"):
            line = line.split("#", 1)[0].strip()
            if line:
                blocked.add(line.lower())

    shown = []
    for c in contributors():
        login = c["login"]
        if c.get("type") != "User" or login.lower() in blocked:
            print(f"skip   {login} (bot or blocklist)")
            continue
        if has_default_avatar(c["avatar_url"]):
            print(f"skip   {login} (default avatar)")
            continue
        print(f"show   {login}")
        shown.append(c)

    cells = [
        f'<a href="{c["html_url"]}" title="{c["login"]}">'
        f'<img src="{c["avatar_url"]}&s={SIZE * 2}" width="{SIZE}" height="{SIZE}" alt="{c["login"]}"></a>'
        for c in shown
    ]
    rows = ["  " + "\n  ".join(cells[i:i + PER_ROW]) for i in range(0, len(cells), PER_ROW)]
    grid = f'{START}\n<p align="center">\n' + "\n  <br>\n".join(rows) + f"\n</p>\n{END}"

    text = open(README, encoding="utf-8").read()
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit("Contributor markers not found in README.md")
    new = pattern.sub(lambda _: grid, text)
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
        print(f"README.md updated: {len(shown)} contributors shown.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    main()
