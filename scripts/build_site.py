"""Turn reports/ci_report.md into a simple static page at site/index.html."""
import html
from pathlib import Path

SRC = Path("reports/ci_report.md")
OUT = Path("site/index.html")


def to_html(markdown: str) -> str:
    body, in_list = [], False
    for line in markdown.splitlines():
        if line.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{html.escape(line[2:])}</li>")
            continue
        if in_list:
            body.append("</ul>")
            in_list = False
        if line.startswith("## "):
            body.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("# "):
            body.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.strip():
            body.append(f"<p>{html.escape(line)}</p>")
    if in_list:
        body.append("</ul>")
    return (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<title>CI Delivery Report</title>"
        "<style>body{font-family:Arial,sans-serif;max-width:640px;margin:3rem auto;padding:0 1rem}"
        "h1{color:#1F3864}</style></head><body>" + "\n".join(body) + "</body></html>"
    )


def main() -> None:
    text = SRC.read_text() if SRC.exists() else "# CI Delivery Report\n\nNo runs recorded yet.\n"
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(to_html(text))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
