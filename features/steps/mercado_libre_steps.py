from selenium import webdriver
from behave import given, when, then
from pages.mercado_libre_page import SearchProduct, ProductsResults

@given('El usuario está en la pantalla de inicio de Mercado Libre')
def step_given_search_wiki(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.mercado_libre_page = SearchProduct(context.driver)

@when('El usuario escribe el término "iPhone 13" en la barra de búsqueda')
def step_when_search_wiki(context):
    context.mercado_libre_page.search("iPhone 13")

@then('El usuario encuentra productos que contienen el texto "iPhone"')
def step_then_search_wiki(context):
    context.mercado_libre_page = ProductsResults(context.driver)
    assert context.mercado_libre_page.isProductPresent("iPhone"), "No se encontró un producto que contenga 'iPhone'"