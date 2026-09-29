def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    filtrados = filter(fn_predicado, lista)
    transformados = map(fn_transformacion, filtrados)

    return list(transformados)


resultado = procesar_coleccion(
    [10, 15, 20, 25, 30],
    lambda x: x > 15,
    lambda x: x * 2
)

print(resultado)