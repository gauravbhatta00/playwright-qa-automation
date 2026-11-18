import os
import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chromium"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False
    )


@pytest.fixture
def page(request):

    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    with sync_playwright() as p:

        browser_type = getattr(p, browser_name)

        browser = browser_type.launch(headless=headless)

        page = browser.new_page()

        yield page

        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)




@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        page.screenshot(
            path=f"screenshots/{request.node.name}.png",
            full_page=True
        )

    