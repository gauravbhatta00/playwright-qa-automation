from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.set_content("""
        <h1>Loading...</h1>

        <script>
            setTimeout(() => {
                document.querySelector("h1").innerText =
                    "Data Loaded Successfully";
            }, 3000);
        </script>
    """)

    heading = page.locator("h1")

    expect(heading).to_have_text("Data Loaded Successfully")

    print("Test Passed!")

    browser.close()