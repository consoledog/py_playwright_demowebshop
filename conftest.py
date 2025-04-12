import logging
import pytest
import allure
from playwright.sync_api import sync_playwright

# This file sets up fixtures for browser contexts, 
# logging, and screenshot capture on failure

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/test.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


# This function tells Pytest to add a new command-line option (--browser) when running tests.
# When running tests, you can pass --browser firefox to override the default and run tests in Firefox.
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chromium", help="browser: chromium, firefox, or webkit"
    )


# This fixture creates and yields a playwright instance from sync_playwright
# The fixture is defined with a session scope. 
# This means it will be instantiated once per test session rather than for each individual test.
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

# The fixture is function-scoped (a new instance for every test function).
# The fixture is parametrized, so there are 3 browsers then each test will run 3 times
# (For each of the browsers)
@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
def browser(request, playwright_instance):
    browser_name = request.param
    logger.info(f"Starting browser: {browser_name}")

    # Launch the browser in headless mode
    browser = getattr(playwright_instance, browser_name).launch(headless=True)
    # Creates an isolated browser context. This is similar to opening a new user session with separate cookies and cache.
    context = browser.new_context()
    page = context.new_page()
    
    yield page # yield page makes the page object available to the test.

    # Capture screenshot on failure if available in test report
    if request.node.rep_call.failed:
        screenshot_path = f"logs/{request.node.name}_{browser_name}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
        logger.error(f"Test {request.node.name} failed in {browser_name}. Screenshot captured: {screenshot_path}")
    context.close()
    browser.close()

 # This hook is used to capture the outcome of each test (pass, fail, skip). 
 # This information is then attached to the test item so that other fixtures 
 # (like the browser fixture) can use this data 
 # (for example, to decide if a screenshot should be taken on failure).
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
