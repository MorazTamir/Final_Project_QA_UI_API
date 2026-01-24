from selenium import webdriver
from selenium.common import WebDriverException

class BrowserWrapperClass:

    def __init__(self):
        print('Test Start!')
        self.driver = None

    def get_driver(self, browser: str, url: str):
        try:
            if browser.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                raise ValueError(f"Browser {browser} is not supported")

            self.driver.get(url)
            self.driver.maximize_window()
            return self.driver

        except WebDriverException as e:
            raise RuntimeError(f"Failed to start browser: {e}")

    def close_browser(self):
        print("Test finish")
        if self.driver:
            self.driver.quit()
