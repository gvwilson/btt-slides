# Tutorial information
title = "Building Tech Together"
slug = "btt-slides"
repo = f"https://github.com/gvwilson/{slug}"
site = f"https://gvwilson.github.io/{slug}"
author = {
    "name": "Greg Wilson",
    "email": "gvwilson@third-bit.com",
    "site": "https://third-bit.com/",
}
lang = "en"
highlight = "tango.css"

chapters = [
    "intro",
    "cogload",
    "meetings",
    "decomp",
    "teaming",
    "grading",
    "process",
    "property",
    "demo",
    "delivery",
    "retro",
    "governance",
    "finale",
]

appendices = [
    "license",
    "conduct",
    "contrib",
    "bib",
    "glossary",
    "colophon",
    "contents",
]

# What to copy.
copy = [
    "*.jpg",
    "*.png",
    "*.svg",
]

# Files and directories to skip.
exclude = {}

# Theme information.
theme = "mccole"
src_dir = "src"
out_dir = "docs"
extension = "/"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}

# Show theme.
if __name__ == "__main__":
    print(theme)
