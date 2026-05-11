import os
from pages.products_page import ProductsPage

def test_ui_displpays_products(driver):
    page = ProductsPage(driver)

    file_path = "file://" + os.path.abspath("ui/index.html")
    page.open(file_path)

    products = page.get_products()

    print("\nProducts from UI")
    for product in products[ :5]:
        print(f"{product['title']} - ${product['price']}")
    
    assert len(products) > 0, "No products displayed on UI"