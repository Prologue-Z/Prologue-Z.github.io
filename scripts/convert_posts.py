"""Convert Hexo blog posts to Hugo format (front-matter only, body untouched)."""
import os
import re
import sys

SRC = "source/_posts"
DST = "content/posts"

def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if not val:
            continue
        fm[key] = val
    return fm, text[m.end():]

def parse_list(val):
    # Handles: [a, b, c] / [a，b] / "single item"
    val = val.strip()
    if val.startswith("["):
        inner = val[1:-1]
        parts = [p.strip().strip('"').strip("'") for p in re.split(r"[,，]", inner)]
        return [p for p in parts if p]
    return [val.strip('"').strip("'")]

def yaml_str(s):
    s = s.strip()
    if not s:
        return '""'
    if s.startswith(("[", "{")) or ":" in s or s.startswith(("-", ">", "|", "&", "*", "!")) or re.search(r'[#\\]', s) or s in ("yes", "no", "true", "false", "null", "~", "on", "off"):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s

def build_front_matter(fm, slug, old_url):
    lines = ["---"]
    title = fm.get("title", "").strip()
    lines.append(f"title: {yaml_str(title)}")
    date = fm.get("date", "").strip().replace(" ", "T")
    if date:
        lines.append(f"date: {yaml_str(date)}")
    updated = fm.get("updated", "").strip().replace(" ", "T")
    if updated:
        lines.append(f"lastmod: {yaml_str(updated)}")
    tags = parse_list(fm.get("tags", "")) if fm.get("tags") else []
    if tags:
        lines.append("tags: [" + ", ".join(yaml_str(t) for t in tags) + "]")
    cats = parse_list(fm.get("categories", "")) if fm.get("categories") else []
    if cats:
        lines.append("categories: [" + ", ".join(yaml_str(c) for c in cats) + "]")
    if fm.get("draft", "").strip() == "true":
        lines.append("draft: true")
    lines.append(f"slug: {yaml_str(slug)}")
    if old_url:
        lines.append(f"aliases: [{yaml_str(old_url)}]")
    lines.append("---")
    return "\n".join(lines)

def main():
    os.makedirs(DST, exist_ok=True)
    count = 0
    for fname in sorted(os.listdir(SRC)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(SRC, fname)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        fm, body = parse_front_matter(text)
        if fm is None:
            print(f"SKIP (no front matter): {fname}")
            continue
        base = fname[:-3]
        slug = re.sub(r"\s+", "-", base)
        fm_date = fm.get("date", "").strip().split(" ")[0]
        old_url = None
        if fm_date:
            y, m, d = fm_date.split("-")
            old_url = f"/{y}/{m}/{d}/{base}/"
        out = build_front_matter(fm, slug, old_url) + "\n\n" + body
        dst = os.path.join(DST, fname)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(out)
        count += 1
        print(f"OK {fname}  ->  /posts/{slug}/  alias={old_url}")
    print(f"\n{count} posts converted")

if __name__ == "__main__":
    main()
