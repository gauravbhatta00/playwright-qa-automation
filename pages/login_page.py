from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

        return DashboardPage(self.page)