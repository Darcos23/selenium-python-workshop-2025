Feature: Buscar un producto en Marcado Libre
    Scenario: Busqueda exitosa de un producto en Mercado Libre
        Given El usuario está en la pantalla de inicio de Mercado Libre
        When El usuario escribe el término "iPhone 13" en la barra de búsqueda
        Then El usuario encuentra productos que contienen el texto "iPhone"