"""Extract full project page content from deployed gh-pages HTML and emit Hugo markdown."""
import re
import subprocess
import sys

PAGES = {
    "almd-control": {
        "title": "连续体机器人自适应动力学建模与控制",
        "description": "自适应集总参数动力学模型（ALMD）与基于模型的前馈控制，发表于 Mechanism and Machine Theory 2024",
        "date": "2024-10-01",
        "tags": ["连续体机器人", "动力学建模", "自适应控制"],
    },
    "variable-gain": {
        "title": "基于速度敏感性的连续体机器人变增益控制",
        "description": "速度敏感性分析与变增益控制策略，发表于 Mechanism and Machine Theory 2022",
        "date": "2022-02-01",
        "tags": ["连续体机器人", "变增益控制", "速度敏感性"],
    },
    "dual-rotational-dofs": {
        "title": "集成双旋转自由度的连续体机器人设计与控制",
        "description": "集成双旋转自由度的连续体机器人机构设计与运动控制，发表于 IEEE IROS 2025",
        "date": "2025-10-01",
        "tags": ["连续体机器人", "双旋转自由度", "运动控制"],
    },
    "cyclotomic-model": {
        "title": "连续体机器人环链式运动学模型及在刚柔混合臂中的应用",
        "description": "环链式运动学模型与刚柔混合臂系统应用，发表于 IEEE ROBIO 2025",
        "date": "2025-12-01",
        "tags": ["连续体机器人", "环链式运动学", "刚柔混合臂"],
    },
}

def get_html(name):
    return subprocess.run(
        ["git", "show", f"gh-pages:projects/{name}.html"],
        capture_output=True, text=True, encoding="utf-8",
    ).stdout

def convert(html):
    # isolate articleBody
    m = re.search(r'<div[^>]*itemprop="articleBody"[^>]*>(.*?)</div>', html, re.S)
    body = m.group(1) if m else html

    out = []
    # split by top-level sections, process each HTML block
    for block in re.split(r'(<h2[^>]*>.*?</h2>)', body, flags=re.S):
        block = block.strip()
        if not block:
            continue
        h2 = re.match(r'<h2[^>]*>(.*?)</h2>', block, re.S)
        if h2:
            title = inline(h2.group(1))
            out.append(f"\n## {title}\n")
            continue
        out.append(process_block(block))
    return "\n".join(out)

def inline(s):
    def link(m):
        href = m.group(1)
        text = inline(m.group(2))
        if href.startswith("#") or not text:
            return text
        return f"[{text}]({href})"
    s = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', link, s, flags=re.S)
    s = re.sub(r'<strong>(.*?)</strong>', lambda m: f"**{inline(m.group(1))}**", s, flags=re.S)
    s = re.sub(r'<em>(.*?)</em>', lambda m: f"*{inline(m.group(1))}*", s, flags=re.S)
    s = re.sub(r'<br\s*/?>', "\n", s)
    s = re.sub(r'<[^>]+>', "", s)
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return s

ELEM_RE = re.compile(
    r'(<h3[^>]*>.*?</h3>|<video.*?</video>|<table.*?</table>|<blockquote.*?</blockquote>'
    r'|<ul>.*?</ul>|<ol>.*?</ol>|<p>.*?</p>|<p[^>]*>.*?</p>|<hr\s*/?>)',
    re.S,
)

def process_elem(el):
    el = el.strip()
    if re.match(r'<hr', el):
        return "\n---\n"
    if re.match(r'<h3', el):
        t = re.match(r'<h3[^>]*>(.*?)</h3>', el, re.S)
        return f"### {inline(t.group(1))}\n" if t else ""
    if re.match(r'<video', el):
        return el + "\n"
    if re.match(r'<table', el):
        return "\n" + el + "\n"
    if re.match(r'<blockquote', el):
        inner = re.sub(r'<blockquote[^>]*>|</blockquote>', "", el, flags=re.S)
        lines = [f"> {inline(l)}" for l in inner.splitlines() if l.strip()]
        return "\n".join(lines) + "\n"
    if re.match(r'<ul', el):
        items = re.findall(r'<li>(.*?)</li>', el, re.S)
        return "\n".join(f"- {inline(i)}" for i in items) + "\n"
    if re.match(r'<ol', el):
        items = re.findall(r'<li>(.*?)</li>', el, re.S)
        return "\n".join(f"{n}. {inline(i)}" for n, i in enumerate(items, 1)) + "\n"
    if re.match(r'<p', el):
        imgs = re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>', el)
        if imgs and re.search(r'<em>', el):
            src, alt = imgs[0]
            cap = re.search(r'<em>(.*?)</em>', el, re.S)
            cap_txt = inline(cap.group(1)) if cap else ""
            return f"![{alt}]({src})\n\n*{cap_txt}*\n"
        if imgs:
            src, alt = imgs[0]
            return f"![{alt}]({src})\n"
        return inline(el) + "\n"
    return inline(el) + "\n"

def process_block(block):
    parts = ELEM_RE.split(block)
    out = []
    for el in parts:
        el = el.strip()
        if not el:
            continue
        if el.startswith("<"):
            out.append(process_elem(el))
        else:
            out.append(inline(el) + "\n")
    return "\n".join(out)

def build_page(name, spec):
    html = get_html(name)
    md = convert(html)
    md = re.sub(r"^\*最后更新：.*$", "", md, flags=re.M)
    md = md.strip() + "\n"
    # add related links footer
    tags = ", ".join(f'"{t}"' for t in spec["tags"])
    fm = (
        "---\n"
        f'title: "{spec["title"]}"\n'
        f'description: "{spec["description"]}"\n'
        f'date: {spec["date"]}\n'
        f"tags: [{tags}]\n"
        f'categories: ["科研项目"]\n'
        'layout: "simple"\n'
        "---\n"
    )
    footer = (
        "\n---\n\n## 🔗 相关链接\n\n"
        "- [返回项目列表](/projects/)\n"
        "- [查看论文页面](/publications/)\n"
        "\n---\n\n*最后更新：2026 年 8 月*\n"
    )
    with open(f"content/projects/{name}.md", "w", encoding="utf-8") as f:
        f.write(fm + "\n" + md + footer)

if __name__ == "__main__":
    for name, spec in PAGES.items():
        build_page(name, spec)
        print(f"built {name}")

def _debug():
    html = get_html("almd-control")
    m = re.search(r'<div[^>]*itemprop="articleBody"[^>]*>(.*?)</div>', html, re.S)
    body = m.group(1)
    idx = body.find("主要挑战")
    with open("/tmp/debug_ctx.txt", "w", encoding="utf-8") as f:
        f.write(body[idx-200:idx+700])

if __name__ == "__main__":
    _debug()
