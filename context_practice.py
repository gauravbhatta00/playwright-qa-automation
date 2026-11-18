from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    # Create two independent contexts
    context1 = browser.new_context()
    context2 = browser.new_context()

    # Add a cookie to context1 only
    context1.add_cookies([
        {
            "name": "role",
            "value": "Admin",
            "url": "https://example.com"
        }
    ])
    context2.add_cookies([
        {
            "name": "role",
            "value": "Student",
            "url": "https://example.com"
        }
    ])

    # Read cookies from both contexts
    print("Context 1:", context1.cookies("https://example.com"))
    print("Context 2:", context2.cookies("https://example.com"))

    context1.close()
    context2.close()
    browser.close()