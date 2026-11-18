
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Create a sample HTML page
    page.set_content("""
        <html>
        <body>
            <h1>Login Form</h1>

            <input id="username" placeholder="Enter username">

            <input id="password" type="password"
                   placeholder="Enter password">

            <button id="login">Login</button>

            <p id="result"></p>

            <script>
                document.querySelector("#login").addEventListener(
                    "click", function() {
                        document.querySelector("#result").innerText =
                            "Login button clicked!";
                    }
                );
            </script>
        </body>
        </html>
    """)

    # Locate input fields and enter information
    page.locator("#username").fill("Gaurav")
    page.locator("#password").fill("123456")

    # Locate and click the login button
    page.locator("#login").click()

    # Print the result
    print(page.locator("#result").inner_text())

    browser.close()
