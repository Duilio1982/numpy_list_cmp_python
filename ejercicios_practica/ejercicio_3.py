# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Práctica de comprensión de listas
    # 1)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá tener un tamaño de 11
    # números, conteniendo del 0 al 10 inclusive

    # lista_0_10 = [......]

    lista_0_10  = [ x  for  x  in  range ( 11 )]
    print ( 'Lista del 0 al 10: ' , lista_0_10 )

    # 2)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener la tabla del 5,
    # desde el múltiplo 0 al múltiplo 10
    # El resultado esperado es:
    # [0 5 10 15 20 25 30 35 40 45 50]
    # Utilizar comprensión de listas para generar esa lista
    # Lo esperable es que realicen una lista de 11 elementos,
    # del 0 al 10 (como el ejer anterior) pero que cada
    # elemento lo multipliquen x5.

    # tabla_5 = [......]

    tabla_5  = [ 5 * x  for x  in  lista_0_10]
    print ( 'Tabla del 5: ' , tabla_5 ) 

    # 3)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener 10 números aleatorios,
    # estos números deberán estar entre el rango 1 al 30 representando
    # números posibles de un mes (los números pueden repetirse).
    # NOTA: Importar el módulo random y utilizar randrange
    # o randint para generar números aleatorios.
    # https://docs.python.org/3/library/random.html

    # dias_mes = [.....]

    import random

    dia_mes  = [ random.randint ( 1 , 30 ) for x in range ( 10 )]
    print ( 'Lista de diez números aleatorios de un mes: ' , dia_mes )

    print("terminamos")