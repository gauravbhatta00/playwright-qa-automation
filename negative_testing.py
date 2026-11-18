from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.set_content("""
        <form>
            <input id="email" type="email" required>
            <button type="submit">Register</button>
            <p id="error" style="display:none;">
                Please enter a valid email.
            </p>
        </form>
    """)

    expect(page.locator("#email")).to_be_visible()
    expect(page.locator("#error")).not_to_be_visible()
    expect(page.locator("#email")).to_be_required()
    page.locator("#email").fill("invalid-email")
    expect(page.locator("#email")).to_have_value("invalid-email")
    # Write your test here

    browser.close()