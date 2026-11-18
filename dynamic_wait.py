from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.set_content("""
        <button onclick="showMessage()">Load Data</button>
        <p id="result" style="display:none;">Data Loaded!</p>

        <script>
            function showMessage() {
                setTimeout(() => {
                    document.querySelector("#result").style.display = "block";
                }, 2000);
            }
        </script>
    """)

    page.get_by_role("button", name="Load Data").click()

    result = page.locator("#result")

    result.wait_for(state="visible")

    print("Message:", result.inner_text())

    browser.close()