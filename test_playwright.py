from playwright.sync_api import sync_playwright, expect


def test_page_title():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()

        page.set_content("""
            <html>
                <head>
                    <title>Student Portal</title>
                </head>
                <body>
                    <h1>Welcome Student</h1>
                </body>
            </html>
        """)

        expect(page).to_have_title("Studentss Portal")
    finally:
        browser.close()