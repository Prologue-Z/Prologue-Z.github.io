"""Fix project page images (shrink via class) and URL-encode file links."""
import re
from urllib.parse import quote

FILES = [
    "content/projects/almd-control.md",
    "content/projects/variable-gain.md",
    "content/projects/dual-rotational-dofs.md",
    "content/projects/cyclotomic-model.md",
    "content/publications.md",
]

def encode_path(path):
    return quote(path, safe="/?=&:._-")

for path in FILES:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    orig = text
    text = re.sub(
        r'!\[([^\]]*)\]\((/images/projects/[^)]+)\)',
        lambda m: f'<img class="project-figure" src="{m.group(2)}" alt="{m.group(1)}" loading="lazy">',
        text,
    )
    text = re.sub(
        r'\]\((/files/[^)]+)\)',
        lambda m: f"]({encode_path(m.group(1))})",
        text,
    )
    if text != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"fixed {path}")
    else:
        print(f"unchanged {path}")
