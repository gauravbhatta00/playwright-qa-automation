from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context1 = browser.new_context()
    context2 = browser.new_context()

    page1 = context1.new_page()
    page2 = context2.new_page()

    page1.goto("https://example.com")
    page2.goto("https://example.com")

    page1.evaluate("""
        localStorage.setItem('username', 'Gaurav');
        sessionStorage.setItem('role', 'admin');
    """)

    username = page2.evaluate("localStorage.getItem('username')")
    role = page2.evaluate("sessionStorage.getItem('role')")

    print("Context 2 Username:", username)
    print("Context 2 Role:", role)

    browser.close()