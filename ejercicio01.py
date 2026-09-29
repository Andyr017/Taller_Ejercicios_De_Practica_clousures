def crear_formateador(prefijo, fn_transformacion):
    def formatear(texto):
        return prefijo + fn_transformacion(texto)

    return formatear


transformar = lambda texto: texto.upper()

formateador = crear_formateador("Resultado: ", transformar)

print(formateador("hola mundo"))