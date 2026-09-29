def crear_pipeline(*funciones_transformacion):
    def ejecutar(dato):
        resultado = dato

        for funcion in funciones_transformacion:
            resultado = funcion(resultado)

        return resultado

    return ejecutar


sumar_dos = lambda x: x + 2
multiplicar_por_tres = lambda x: x * 3
restar_uno = lambda x: x - 1

pipeline = crear_pipeline(
    sumar_dos,
    multiplicar_por_tres,
    restar_uno
)

print(pipeline(5))