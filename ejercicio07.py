def crear_acumulador_validado(criterio_lambda):
    total = 0

    def acumular(valor):
        nonlocal total

        if criterio_lambda(valor):
            total += valor

        return total

    return acumular


criterio = lambda valor: valor > 10

acumulador = crear_acumulador_validado(criterio)

print(acumulador(5))
print(acumulador(20))
print(acumulador(8))
print(acumulador(30))