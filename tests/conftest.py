import pytest
from base.webdriverfactory import WebDriverFactory
import time



@pytest.yield_fixture(scope="function")
#@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser,url):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    driver.get(url)
    driver.implicitly_wait(10)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")