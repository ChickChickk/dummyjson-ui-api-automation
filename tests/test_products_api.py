from api.products_api import ProductsAPI

def test_get_all_products():
    api = ProductsAPI()

    data = api.get_all_products()
    products = data["products"]

    print("\nFirst 5 products from API:")
    for product in products[ :5]:
        print(f"{product['title']} - ${product['price']}")
    
    assert len(products) > 0, "No products returned from API"

def test_get_product_by_id():
    api = ProductsAPI()

    product = api.get_product_by_id(1)

    print("\nSingle product:")
    print(product['title'], product["price"])

    assert product["id"] == 1
    assert "title" in product
    assert "price" in product
