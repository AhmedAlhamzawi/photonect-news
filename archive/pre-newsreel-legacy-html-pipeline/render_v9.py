import asyncio
import os
from pyppeteer import launch

OUTPUT_DIR = "/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/slides_v9"
HTML_PATH = "file:///Users/ahmed/Desktop/Photonect%20NEWS/NEWS%20CODE/iraq_v9.html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

async def render():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    browser = await launch(
        headless=True,
        executablePath=CHROME,
        args=['--no-sandbox', '--disable-setuid-sandbox']
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1080, 'height': 1080, 'deviceScaleFactor': 2})
    await page.goto(HTML_PATH, {'waitUntil': 'networkidle0', 'timeout': 30000})
    await asyncio.sleep(5)  # Wait for fonts to load fully

    for i in range(1, 7):
        slide_id = f"slide{i}"
        element = await page.querySelector(f"#{slide_id}")
        if element:
            out_path = os.path.join(OUTPUT_DIR, f"slide_{i:02d}.png")
            await element.screenshot({'path': out_path, 'type': 'png'})
            print(f"OK slide {i} -> {out_path}")
        else:
            print(f"ERROR: #{slide_id} not found")

    await browser.close()
    print("All slides rendered.")

asyncio.run(render())
