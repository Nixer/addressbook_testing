from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(ChromeDriverManager().install())
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            False

    def open_home_page(self):
        wd = self.wd
        wd.get('http://17.218.71.53/addressbook/')

    def destroy(self):
        self.wd.quit()
