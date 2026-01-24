# import unittest
# from logic.apis.products_api import ProductsApi
# from logic.UI_Pages.products_page import ProductsPage
# from infra.UI.browser_wrapper import BrowserWrapperClass
#
#
# class ProductsTest(unittest.TestCase):
#
#     def setUp(self):
#         self.browser = BrowserWrapperClass()
#         self.driver = self.browser.get_driver(
#             'Chrome',
#             'https://practicesoftwaretesting.com'
#         )
#
#     def test_product_from_api_exists_in_ui(self):
#
#         # API
#         api_response = ProductsApi.get_all_products()
#         product_name = api_response.data["data"][0]["name"]
#
#         # UI
#         products_page = ProductsPage(self.driver)
#         products_page.open_products_page()
#
#         self.assertIn(
#             product_name,
#             products_page.get_all_product_names()
#         )
#
#     def tearDown(self):
#         self.driver.quit()
