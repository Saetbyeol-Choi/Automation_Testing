# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     context = browser.new_context(viewport={"width": 1500, "height": 1000})
#     page = context.new_page()
#
#     # Retrieving viewport size
#     width = page.viewport_size["width"]
#     height = page.viewport_size["height"]
#     print(f"Viewport size: {width} x {height}")
#
#     # Change viewport size
#     context.viewport_size = {"width": 1920, "height": 1080}
#
#     # Retrieving updated viewport size
#     width = page.viewport_size["width"]
#     height = page.viewport_size["height"]
#     print(f"Updated viewport size: {width} x {height}")
#
#     # Rest of your testing code goes here
#
#     browser.close()
