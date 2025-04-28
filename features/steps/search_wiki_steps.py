from selenium import webdriver
from behave import given, when, then
from pages.search_wiki_page import SearchWikiArticle, WikiArticle

@given('El usuario está en la pantalla de inicio de Wikipedia')
def step_given_search_wiki(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')
    context.search_wiki_page = SearchWikiArticle(context.driver)

@when('El usuario escribe el término "Python (lenguaje de programación)" en la barra de búsqueda')
def step_when_search_wiki(context):
    context.search_wiki_page.search("Python (lenguaje de programación)")

@then('El usuario encuentra el artículo titulado Python')
def step_then_search_wiki(context):
    context.search_wiki_page2 = WikiArticle(context.driver)
    assert "Python" == context.search_wiki_page2.isTitlePresent()