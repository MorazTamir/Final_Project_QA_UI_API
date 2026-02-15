import unittest
import time

from infra.UI.base_page import BasePage
from infra.UI.browser_wrapper import BrowserWrapperClass
from logic.UI_Pages.contact_page import ContactPage
from logic.APIs.contact_api import CaontactApi


class ContactHybridTests(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapperClass()
        self.driver = self.browser.get_driver('Chrome', 'https://practicesoftwaretesting.com/contact')
        # uniq mail
        self.unique_email = f"test_{int(time.time())}@gmail.com"

    def test_contact_submission_flow(self):
        base_page = BasePage(self.driver)
        base_page.click_contact()
        long_msg = "A" * 55

        contact_page = ContactPage(self.driver)
        #Step 1: UI - fill form
        contact_page.first_name_fill_text("Omer")
        contact_page.last_name_fill_text("Automation")
        contact_page.email_fill_text(self.unique_email)
        contact_page.select_subject('Customer service')
        contact_page.msg_fill_text(long_msg)
        contact_page.click_submit_btn()

        # Wait for Server
        time.sleep(2)

        # API Validation
        api_response = CaontactApi.get_messages()
        self.assertTrue(api_response.ok, "API call failed")
        messages_list = api_response.data["data"]
        found_message = next((m for m in messages_list if m["email"] == self.unique_email), None)
        self.assertIsNotNone(found_message, f"Message with email {self.unique_email} was not found in API")

    def tearDown(self):
        self.browser.close_browser()