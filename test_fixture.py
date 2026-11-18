import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture
def browser_page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()


def test_heading(browser_page):

    browser_page.set_content("<h1>Welcome Student</h1>")

    expect(browser_page.locator("h1")).to_have_text("Welcome Student")


def test_button(browser_page):

    browser_page.set_content("<button>Login</button>")

    expect(browser_page.get_by_role("button", name="Login")).to_be_visible()