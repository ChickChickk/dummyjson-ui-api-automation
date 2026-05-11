import os 

from api.products_api import ProductsAPI
from pages.products_page import ProductsPage

def test_ui_products_match_api_products(driver):
    page = ProductsPage(driver)
    api = ProductsAPI()

    file_path = "file://" + os.path.abspath("ui/index.html")
    page.open(file_path)

    ui_products = page.get_products()
    api_data = api.get_all_products()
    api_products = api_data["products"][: 10]

    print("\nComparing UI Products with API Products:")

    for ui_product, api_product in zip(ui_products, api_products):
        print(f"UI: {ui_product['title']} - {ui_product['price']}")
        print(f"API: {api_product['title']} - {api_product['price']}")
        print("---")

        assert ui_product["title"] == api_product["title"]
        assert float(ui_product["price"]) == float(api_product['price'])

    assert len(ui_products) == len(api_products)