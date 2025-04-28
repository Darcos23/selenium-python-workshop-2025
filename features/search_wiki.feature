Feature: Buscar artículo en Wikipedia a partir de su nombre
    Scenario: Busqueda exitosa de un artículo en Wikipedia
        Given El usuario está en la pantalla de inicio de Wikipedia
        When El usuario escribe el término "Python (lenguaje de programación)" en la barra de búsqueda
        Then El usuario encuentra el artículo titulado Python