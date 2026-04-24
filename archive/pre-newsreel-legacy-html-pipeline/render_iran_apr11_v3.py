import asyncio
import os
from pyppeteer import launch

HTML_FILE = os.path.abspath("iran_war_apr11_v3.html")
OUTPUT_DIR = os.path.abspath("iran_apr11_v3_slides")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SLIDES = [
    ("slide-1", "01_cover"),
    ("slide-2", "02_islamabad_talks"),
    ("slide-3", "03_lost_mines_map"),
    ("slide-4", "04_frozen_assets"),
    ("slide-5", "05_saudi_oil"),
    ("slide-6", "06_lebanon"),
    ("slide-7", "07_sources"),
]

async def render():
    browser = await launch(
        executablePath=CHROME_PATH,
        headless=True,
        args=[
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu',
            '--font-render-hinting=none',
        ]
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1080, 'height': 1080, 'deviceScaleFactor': 2})
    await page.goto(f'file://{HTML_FILE}', {'waitUntil': 'networkidle0', 'timeout': 30000})

    # Wait for Google Fonts to load
    await asyncio.sleep(4)

    for slide_id, filename in SLIDES:
        element = await page.querySelector(f'#{slide_id}')
        if element:
            out_path = os.path.join(OUTPUT_DIR, f"{filename}.png")
            await element.screenshot({'path': out_path})
            print(f"✓ Rendered: {filename}.png")
        else:
            print(f"✗ NOT FOUND: #{slide_id}")

    await browser.close()
    print(f"\nAll done! Slides saved to: {OUTPUT_DIR}")

asyncio.run(render())
