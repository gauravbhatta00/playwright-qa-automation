from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # First context
    context1 = browser.new_context()
    page1 = context1.new_page()

    page1.goto("https://example.com")

    # Save some localStorage data
    page1.evaluate("""
        localStorage.setItem('username', 'Gaurav');
    """)

    # Save browser state
    context1.storage_state(path="auth.json")

    # Create a new context using saved state
    context2 = browser.new_context(storage_state="auth.json")
    page2 = context2.new_page()

    page2.goto("https://example.com")

    username = page2.evaluate(
        "localStorage.getItem('username')"
    )

    print("Restored username:", username)

    browser.close()