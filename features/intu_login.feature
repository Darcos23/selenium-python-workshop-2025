Feature: Login de Intu
    Scenario: Credenciales Incorrectas Intu
        Given El usuario se encuentra en la pagina de Login de Intu
        When El usuario escribe credenciales erroneas
        Then aparece un mensaje de error