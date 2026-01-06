from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from config.config_provider import ConfigProvider

class BrowserWrapperClass:
    def __init__(self):
        print('Test Start!')
        self.driver = None
        self.config = ConfigProvider()

    def get_driver(self):
        browser = self.config.get_browser()
        url = self.config.get_base_url()
        try:
            if browser.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            self.driver.get(url)
            self.driver.maximize_window()
            return self.driver
        except WebDriverException as e:
            print(f"WebDriver Exception: {e}")

    def close_browser(self):
        print("Test finish")
        if self.driver:
            self.driver.quit()
