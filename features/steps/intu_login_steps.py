from selenium import webdriver
from behave import given, when, then
from pages.intu_login_page import IntuLogin

@given('El usuario se encuentra en la pagina de Login de Intu')
def step_given_intu_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.icesi.edu.co/moodle/login/index.php')
    context.intu_login_page = IntuLogin(context.driver)

@when('El usuario escribe credenciales erroneas')
def step_when_intu_login(context):
    context.intu_login_page.login("1086133076","abcd12345")

@then('aparece un mensaje de error')
def step_then_intu_login(context):
    assert "Acceso inválido. Por favor, inténtelo otra vez." == context.intu_login_page.isElementPresent()