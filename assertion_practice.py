from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.set_content("""
        <h1>Student Registration</h1>

        <input id="email" type="email" value="student@gmail.com">

        <p id="message">Registration successful!</p>

        <button>Continue</button>
    """)

    # Your assertions go here
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator("#email")).to_have_value("student@gmail.com")
    expect(page.locator("#message")).to_have_text("Registration successful!")
    expect(page.locator("button")).to_be_visible()
    browser.close()