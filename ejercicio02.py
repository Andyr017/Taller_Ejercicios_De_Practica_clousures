def crear_operador(factor, operacion_lambda):
    def operar(valor):
        return operacion_lambda(valor, factor)

    return operar


multiplicar = lambda valor, factor: valor * factor

operador = crear_operador(5, multiplicar)

print(operador(10))