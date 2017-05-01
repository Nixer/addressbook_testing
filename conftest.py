import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    if fixture is None:
         fixture = Application(browser=browser, base_url=base_url, username=username, password=password)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username=username, password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--base_url", action="store", default="http://17.218.71.53/addressbook/")
    parser.addoption("--username", action="store", default="admin")
    parser.addoption("--password", action="store", default="secret")

