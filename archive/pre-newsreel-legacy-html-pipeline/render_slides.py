#!/usr/bin/env python3
"""Render each slide from v3_carousel.html as 1080x1350 PNG using pyppeteer"""
import asyncio
import os

async def main():
    from pyppeteer import launch

    out = "/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/slides_v3"
    os.makedirs(out, exist_ok=True)

    html_path = "file:///Users/ahmed/Desktop/Photonect%20NEWS/NEWS%20CODE/v3_carousel.html"

    print("Launching Chrome...")
    browser = await launch(
        headless=True,
        args=['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none'],
        executablePath='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    )

    page = await browser.newPage()
    await page.setViewport({'width': 1080, 'height': 1350, 'deviceScaleFactor': 2})

    print("Loading page...")
    await page.goto(html_path, {'waitUntil': 'networkidle0', 'timeout': 30000})
    await asyncio.sleep(3)  # Wait for fonts to load

    for i in range(1, 9):
        slide_id = f"slide{i}"
        print(f"  Capturing slide {i}...")

        # Scroll slide into view and capture it
        element = await page.querySelector(f'#{slide_id}')
        if element:
            await element.screenshot({
                'path': os.path.join(out, f'{i:02d}_slide.png'),
                'type': 'png',
            })
            print(f"  Slide {i} saved")
        else:
            print(f"  WARNING: #{slide_id} not found!")

    await browser.close()
    print(f"\nAll slides saved to: {out}")
    for f in sorted(os.listdir(out)):
        if f.endswith('.png'):
            sz = os.path.getsize(os.path.join(out, f))
            print(f"  {f} ({sz//1024}KB)")

asyncio.get_event_loop().run_until_complete(main())
