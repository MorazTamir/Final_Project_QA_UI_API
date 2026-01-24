from infra.API.base_api import BaseApi

class ProductsApi:

    @staticmethod
    def get_all_products():
        return BaseApi.get_api_call('products')

    @staticmethod
    def get_product_by_id(product_id):
        return BaseApi.get_api_call(f'products/{product_id}')

    @staticmethod
    def search_products(query):
        return BaseApi.get_api_call(f'products?q={query}')

    @staticmethod
    def get_products_by_category(category_id):
        return BaseApi.get_api_call(f'products?category={category_id}')

    @staticmethod
    def get_products_by_brand(brand_id):
        return BaseApi.get_api_call(f'products?brand={brand_id}')
