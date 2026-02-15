import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class DropdownComponent:
    def __init__(self, driver, wait, locator):
        self._driver = driver
        self._wait = wait
        self._locator = locator

    def select_by_text(self, txt):
        element = self._wait.until(EC.element_to_be_clickable(self._locator))
        select = Select(element)
        select.select_by_visible_text(txt)

    def select_random(self, ignore_options=None):
        if ignore_options is None:
            ignore_options = ["Choose...", "Select subject"]
        element = self._wait.until(EC.visibility_of_element_located(self._locator))
        select = Select(element)
        valid_options = [opt.text for opt in select.options if opt.text not in ignore_options]
        choice = random.choice(valid_options)
        select.select_by_visible_text(choice)
        return choice