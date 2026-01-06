from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BasePage:
    # Navbar elements XPaths
    LOGO = '//*[@id="navbar"]//a[contains(@class, "navbar-brand")]'
    MAIN_MENU_ITEMS = '//*[@id="navbar"]//ul[contains(@class,"navbar-nav")]/li/a'
    LOGIN_BUTTON = '//*[@id="navbar"]//a[text()="Login"]'
    LANGUAGE_DROPDOWN = '//*[@id="language"]'
    CART_BUTTON = '//*[@id="navbar"]//a[@title="Cart"]'
    HAMBURGER_MENU = '//*[@id="navbar"]//button[contains(@class,"navbar-toggler")]'

    def __init__(self, driver):
        self._driver = driver
        self._logo = self._driver.find_element(By.XPATH, self.LOGO)
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        self._language_dropdown = self._driver.find_element(By.XPATH, self.LANGUAGE_DROPDOWN)
        self._cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)
        self._hamburger_menu = self._driver.find_element(By.XPATH, self.HAMBURGER_MENU)
        self._main_menu_items = self._driver.find_elements(By.XPATH, self.MAIN_MENU_ITEMS)

    # Actions
    def go_to_home(self):
        self._logo.click()

    def click_login(self):
        self._login_button.click()

    def select_language(self, lang_value):
        select = Select(self._language_dropdown)
        select.select_by_value(lang_value)

    def open_cart(self):
        self._cart_button.click()

    def toggle_hamburger_menu(self):
        self._hamburger_menu.click()

    def get_main_menu_items(self):
        return [item.text for item in self._main_menu_items]
