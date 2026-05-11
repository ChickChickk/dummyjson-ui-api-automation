import requests

class ProductsAPI:
    BASE_URL = "https://dummyjson.com"

    def get_all_products(self):
        response = requests.get(f"{self.BASE_URL}/products")
        response.raise_for_status()
        return response.json()
    
    def get_product_by_id(self, product_id):
        response = requests.get(f"{self.BASE_URL}/products/{product_id}")
        response.raise_for_status()
        return response.json()
    