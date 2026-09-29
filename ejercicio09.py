def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0

    def ejecutar(accion="ejecutar"):
        nonlocal intentos

        if accion == "reset":
            intentos = 0
            return "Contador reiniciado"

        intentos += 1

        if intentos > max_intentos:
            return fn_alerta(intentos)

        return f"Ejecución permitida: {intentos}"

    return ejecutar


alerta = lambda intentos: f"Límite superado. Intentos: {intentos}"

limitador = crear_limitador_avanzado(3, alerta)

print(limitador())
print(limitador())
print(limitador())
print(limitador())
print(limitador("reset"))
print(limitador())