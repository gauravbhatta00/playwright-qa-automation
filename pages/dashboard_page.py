from pages.base_page import BasePage
from components.navbar import Navbar


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.logout_button = page.locator("#logout")
        self.message = page.locator("#message")

        self.navbar = Navbar(page)

    def logout(self):
        self.logout_button.click()