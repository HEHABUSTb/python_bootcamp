from dataclasses import dataclass
from playwright.sync_api import Playwright, Page
import pytest



@dataclass
class User:
    email: str
    password: str


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser type"
    )


@pytest.fixture(scope='session')
def user(request) -> User:
    return User(**request.param)


@pytest.fixture
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption('--browser_name')

    browser = None
    match browser_name:
        case 'chrome':
            browser = playwright.chromium.launch(headless=False)
        case 'firefox':
            browser = playwright.firefox.launch(headless=False)
        case _:
            raise NotImplementedError('Wrong browser type: {}'.format(browser_name))


    context = browser.new_context()
    page = context.new_page()

    yield page
    # Tear down section
    context.close()
    browser.close()
