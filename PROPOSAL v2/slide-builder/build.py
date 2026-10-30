"""Render the proposal-defense slide visuals to PNG for PowerPoint.

Each src/slide-*.html is a 1920x1080 (16:9) page. It is captured at 2x, so every
PNG is 3840x2160 and stays sharp on a projector. Insert each PNG as a full-slide
picture in a 16:9 PowerPoint slide.

A slide with <body data-steps="N"> also gets click-to-reveal frames in slides/steps/
(slide-03a-1.png ... slide-03a-<N-1>.png). Put them before the full slide in
PowerPoint with a Fade transition, and each click reveals the next part.

Usage (from any directory):
    python3 build.py              # render every slide
    python3 build.py 01 03a       # render only slides whose number starts with these

Needs Python Playwright and Google Chrome. The pages load fonts and icons from
Google Fonts and unpkg, so the first build needs an internet connection.
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
OUT = HERE.parent / "slides"
STEPS = OUT / "steps"

# Flags any element that spills past the bottom or right edge of the main content
# area, so overflow is caught at build time instead of in the projector.
OVERFLOW_CHECK = """() => {
  const area = document.querySelector('.content') || document.querySelector('.slide');
  const box = area.getBoundingClientRect();
  const hits = [];
  for (const el of area.querySelectorAll('*')) {
    const r = el.getBoundingClientRect();
    if (r.width && (r.bottom > box.bottom + 1 || r.right > box.right + 1)) {
      hits.push(String(el.className.baseVal ?? el.className) || el.tagName);
    }
  }
  return [...new Set(hits)].slice(0, 5);
}"""


# Lucide leaves an <i data-lucide> in place when the icon name doesn't exist.
MISSING_ICONS = """() => [...new Set([...document.querySelectorAll('i[data-lucide]')].map(i => i.dataset.lucide))]"""


def main(selected):
    pages = sorted(SRC.glob("slide-*.html"))
    if selected:
        pages = [p for p in pages if p.stem.removeprefix("slide-").startswith(tuple(selected))]
    if not pages:
        sys.exit("No matching slides in src/.")

    OUT.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome")
        page = browser.new_page(
            viewport={"width": 1920, "height": 1080}, device_scale_factor=2
        )
        for src in pages:
            page.goto(src.as_uri(), wait_until="networkidle")
            page.wait_for_function("window.slideReady === true")
            out = OUT / f"{src.stem}.png"
            page.screenshot(path=str(out))
            overflow = page.evaluate(OVERFLOW_CHECK)
            missing = page.evaluate(MISSING_ICONS)
            note = f"  !! overflow: {', '.join(overflow)}" if overflow else ""
            note += f"  !! unknown icons: {', '.join(missing)}" if missing else ""
            print(f"wrote slides/{out.name}{note}")

            steps = int(page.evaluate("document.body.dataset.steps || 0"))
            if steps > 1:
                STEPS.mkdir(exist_ok=True)
                for n in range(1, steps):
                    page.goto(f"{src.as_uri()}?step={n}", wait_until="networkidle")
                    page.wait_for_function("window.slideReady === true")
                    page.screenshot(path=str(STEPS / f"{src.stem}-{n}.png"))
                print(f"  + {steps - 1} build steps in slides/steps/")
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1:])
