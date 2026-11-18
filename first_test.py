
from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:

    # Launch Chromium
    browser = p.chromium.launch(headless=False)

    context=browser.new_context()
    # Create a new browser tab
    page = context.new_page()

    # Navigate to a website
    page.goto("https://www.example.com")

    # Get page information
    print("Page title:", page.title())
    print("Page URL:", page.url)

    # Take a screenshot
    page.screenshot(path="screenshot.png")
    assert page.title() == "Example Domain"
    context.close()
    # Close browser
    browser.close()
