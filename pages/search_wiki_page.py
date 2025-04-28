import time
from .base_page import BasePage
from selenium.webdriver.common.by import By

class SearchWikiArticle(BasePage):
    SEARCH_ICON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/a')
    SEARCH_FIELD = (By.NAME, 'search')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/button')
    
    def search(self, article):
        self.click(self.SEARCH_ICON)
        self.enter_text(self.SEARCH_FIELD, article)
        self.click(self.SEARCH_BUTTON)
    
class WikiArticle(BasePage):
    TITLE = (By.CLASS_NAME, 'mw-page-title-main')
    
    def isTitlePresent(self):
        time.sleep(3)
        title = self.find_element(self.TITLE)
        texto = title.text
        print(texto)
        return texto