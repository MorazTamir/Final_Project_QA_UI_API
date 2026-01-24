# from selenium.webdriver.common.by import By
# from infra.UI.base_page import BasePage
#
# class ProductsPage(BasePage):
#
#     PRODUCTS_URL = "https://practicesoftwaretesting.com/#/products"
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     # locators
#     PRODUCT_TITLES = (By.CLASS_NAME, "card-title")
#     ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn.btn-primary")
#
#     # actions (business actions)
#     def open_products_page(self):
#         self._driver.get(self.PRODUCTS_URL)
#
#     def get_all_product_names(self):
#         elements = self._driver.find_elements(*self.PRODUCT_TITLES)
#         return [el.text for el in elements]
#
#     def add_first_product_to_cart(self):
#         self._driver.find_elements(*self.ADD_TO_CART_BUTTONS)[0].click()
#
#     def add_product_to_cart_by_name(self, product_name):
#         titles = self._driver.find_elements(*self.PRODUCT_TITLES)
#         buttons = self._driver.find_elements(*self.ADD_TO_CART_BUTTONS)
#
#         for title, button in zip(titles, buttons):
#             if product_name.lower() in title.text.lower():
#                 button.click()
#                 return True
#
#         return False