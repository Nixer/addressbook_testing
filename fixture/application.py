from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url, username, password):
        if browser == "chrome":
            self.wd = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.username = username
        self.password = password

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
