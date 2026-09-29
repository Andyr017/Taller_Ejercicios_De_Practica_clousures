def agrupar_por(lista, fn_clave):
    resultado = {}

    for elemento in lista:
        clave = fn_clave(elemento)

        if clave not in resultado:
            resultado[clave] = []

        resultado[clave].append(elemento)

    return resultado


personas = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Pedro", "edad": 20},
    {"nombre": "Maria", "edad": 25}
]

resultado = agrupar_por(
    personas,
    lambda persona: persona["edad"]
)

print(resultado)