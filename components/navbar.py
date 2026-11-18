class Navbar:

    def __init__(self, page):
        self.page = page

        self.home = page.locator("#home")
        self.profile = page.locator("#profile")
        self.settings = page.locator("#settings")

    def open_home(self):
        self.home.click()

    def open_profile(self):
        self.profile.click()

    def open_settings(self):
        self.settings.click()