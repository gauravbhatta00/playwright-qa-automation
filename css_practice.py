from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()


    page.set_content("""
        <h1 id="heading">Welcome</h1>

        <input id="email" type="email" placeholder="Enter email">

        <input class="password" type="password">

        <button id="submit">Submit</button>""")

    # print(page.locator("#heading").inner_text())
    print(page.get_by_text("Welcome").inner_text())
    # page.locator("#email").fill("student@gmail.com")
    page.get_by_placeholder("Enter email").fill("student@gmail.com")
    page.locator(".password").fill("mypassword123")
    # page.locator("#submit").click()
    page.get_by_role("button", name="Submit").click()
    
    expect(page.get_by_text("Welcome")).to_be_visible()
    browser.close()