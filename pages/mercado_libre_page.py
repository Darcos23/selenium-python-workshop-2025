import time
from .base_page import BasePage
from selenium.webdriver.common.by import By

class SearchProduct(BasePage):
    SEARCH_FIELD = (By.ID, 'cb1-edit')
    SEARCH_BUTTON = (By.CLASS_NAME, 'nav-search-btn')
    
    def search(self, product):
        self.enter_text(self.SEARCH_FIELD, product)
        self.click(self.SEARCH_BUTTON)
    
class ProductsResults(BasePage):
    PRODUCT = (By.CLASS_NAME, 'poly-component__title')
    
    def isProductPresent(self, keyword):
        product = self.find_element(self.PRODUCT)
        texto = product.text.lower()
        if keyword.lower() in texto:
            return True
        return False