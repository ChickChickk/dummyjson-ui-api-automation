from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    product_cards = (By.CSS_SELECTOR, ".product-card")
    product_title = (By.CSS_SELECTOR, ".title")
    product_price = (By.CSS_SELECTOR, ".price")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, file_path):
        self.driver.get(file_path)
    
    def get_product_cards(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located(self.product_cards)
        )
    
    def get_products(self):
        products = []
        cards = self.get_product_cards()

        for card in cards:
            title = card.find_element(*self.product_title).text
            price = card.find_element(*self.product_price).text

            products.append({
                "title": title,
                "price": price
            })
        
        return products