from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BasePage:
    # Navbar elements XPaths
    LOGO_TOOL = '//*[@id="Layer_1"]'
    HOME_HREF = '//*[@id="navbarSupportedContent"]/ul/li[1]/a'
    CATEGORIES_HREF = '//*[@id="navbarSupportedContent"]/ul/li[2]/a'
    CONTACT_HREF = '//a[contains(text(),"Contact")]'
    LOGIN_BUTTON = '//a[@data-test="nav-sign-in"]'
    LANGUAGE_BTN = '//*[@id="language"]'


    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._timeout = timeout
        self._logo = self._driver.find_element(By.XPATH, self.LOGO_TOOL)
        self._home_href = self._driver.find_elements(By.XPATH, self.HOME_HREF)
        self._categories_href = self._driver.find_element(By.XPATH, self.CATEGORIES_HREF)
        self._contact_href = self._driver.find_element(By.XPATH, self.CONTACT_HREF)
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        self._language_dropdown = self._driver.find_element(By.XPATH, self.LANGUAGE_BTN)

    def get_url(self):
        return self._driver.current_url

    def click_home(self):
        self._home_href.click()

    def click_logo(self):
        self._logo.click()

    def click_categories(self): #drop-down component
        self._categories_href.click()

    def click_contact(self):
        self._contact_href.click()

    def click_login(self):
        self._login_button.click()

    def select_language(self, lang_value): #drop-down component
        select = Select(self._language_dropdown)
        select.select_by_value(lang_value)