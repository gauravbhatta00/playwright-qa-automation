
from pages.login_page import LoginPage
from playwright.sync_api import expect
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_execution.log", mode="w"),
        logging.StreamHandler()
    ],
    force=True
)


def test_login_logout(page):

    logging.info("Opening login page")

    page.set_content("""
        <h2>Login Page</h2>

        <input id="username" placeholder="Username">
        <input id="password" type="password" placeholder="Password">

        <button id="login">Login</button>
        <button id="logout">Logout</button>

        <p id="message"></p>

        <script>
            document.querySelector("#login").addEventListener("click", () => {
                document.querySelector("#message").innerText =
                    "Login successful";
            });

            document.querySelector("#logout").addEventListener("click", () => {
                document.querySelector("#message").innerText =
                    "Logged out";
            });
        </script>
    """)

    logging.info("Login page loaded successfully")

    login_page = LoginPage(page)

    logging.info("Performing login")

    dashboard_page = login_page.login("admin", "12345")

    logging.info("Verifying login success")

    expect(dashboard_page.message).to_have_text("Login successful")

    logging.info("Login successful")

    logging.info("Performing logout")

    dashboard_page.logout()

    logging.info("Verifying logout")

    expect(dashboard_page.message).to_have_text("Logged out")

    logging.info("Logout successful")
