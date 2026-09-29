def ejecutar_y_rastrear(fn_tarea, n):
    historial = []

    def ejecutar():
        for _ in range(n):
            historial.append(fn_tarea())

        return historial

    return ejecutar


contador = 0

def tarea():
    global contador
    contador += 1
    return contador


ejecutor = ejecutar_y_rastrear(tarea, 3)

print(ejecutor())