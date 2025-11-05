from pathlib import Path

from playwright.sync_api import sync_playwright


def main() -> None:
    page_width = 1280
    page_height = 720

    html_path = Path("index.html").resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": page_width, "height": page_height})
        page.goto(html_path, wait_until="networkidle")
        page.wait_for_timeout(1000)
        page.screenshot(path="glowing-search.png", full_page=True)
        browser.close()


if __name__ == "__main__":
    main()
