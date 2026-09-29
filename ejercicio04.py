def crear_generador_sufijos(patron_lambda):
    contador = 0

    def generar(nombre):
        nonlocal contador
        contador += 1
        return patron_lambda(nombre, contador)

    return generar


patron = lambda nombre, numero: f"{nombre}_{numero}.txt"

generador = crear_generador_sufijos(patron)

print(generador("documento"))
print(generador("documento"))
print(generador("tarea"))