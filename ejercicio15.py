import time


def auditar_ejecucion(fn_objetivo, fn_logger):
    def ejecutar(*args, **kwargs):
        inicio = time.perf_counter()

        resultado = fn_objetivo(*args, **kwargs)

        fin = time.perf_counter()

        tiempo = fin - inicio

        fn_logger(tiempo, resultado)

        return resultado

    return ejecutar


def registrar(tiempo, resultado):
    print("Resultado:", resultado)
    print("Tiempo de ejecución:", tiempo)


def calcular():
    return sum(range(100000))


funcion_auditada = auditar_ejecucion(calcular, registrar)

print("Retorno:", funcion_auditada())