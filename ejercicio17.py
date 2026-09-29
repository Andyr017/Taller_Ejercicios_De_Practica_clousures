def memoizar_avanzado(fn_costosa, max_items):
    cache = {}

    def ejecutar(valor):
        if valor in cache:
            return cache[valor]

        resultado = fn_costosa(valor)

        if len(cache) >= max_items:
            primer_elemento = next(iter(cache))
            del cache[primer_elemento]

        cache[valor] = resultado

        return resultado

    return ejecutar


def calcular_cuadrado(numero):
    print("Calculando...")
    return numero * numero


cuadrado = memoizar_avanzado(calcular_cuadrado, 2)

print(cuadrado(5))
print(cuadrado(5))
print(cuadrado(10))
print(cuadrado(15))
print(cuadrado(10))