from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from infra.UI.base_page import BasePage

class ContactPage(BasePage):
    CONTACT_HEADER = '//h3[text()="Contact"]'
    FIRST_NAME_INPUT = '//*[@id="first_name"]'
    LAST_NAME_INPUT = '//*[@id="last_name"]'
    EMAIL_INPUT = '//*[@id="email"]'
    SUBJECT_SELECT = '//*[@id="subject"]'
    MSG_INPUT = '//*[@id="message"]'
    SEND_BTN = '//input[@data-test="contact-submit"]'
    ERROR_EMPTY_FIELD = '//*[@id="message.errors"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._contact_header = self._driver.find_element(By.XPATH, self.CONTACT_HEADER)
        self._first_name_input = self._driver.find_element(By.XPATH, self.FIRST_NAME_INPUT)
        self._last_name_input = self._driver.find_element(By.XPATH, self.LAST_NAME_INPUT)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._subject_input = self._driver.find_element(By.XPATH, self.SUBJECT_SELECT)
        self._msg_input = self._driver.find_element(By.XPATH, self.MSG_INPUT)
        self._send_btn = self._driver.find_element(By.XPATH, self.SEND_BTN)

    def get_contact_header_text(self):
        return self._contact_header.text

    def first_name_fill_text(self, name):
        self._first_name_input.send_keys(name)

    def last_name_fill_text(self, name):
        self._last_name_input.send_keys(name)

    def email_fill_text(self, email):
        self._email_input.send_keys(email)

    def select_subject(self, txt): #txt - from json?!
        self._subject_input.click()
        select = Select(self._subject_input)
        select.select_by_visible_text(txt)

    def msg_fill_text(self, msg):
        self._msg_input.send_keys(msg)

    def click_submit_btn(self):
        self._send_btn.click()

    def get_error_msg_text(self):
        return self._driver.find_element(By.XPATH, self.ERROR_EMPTY_FIELD).text