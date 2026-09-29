def crear_validador_múltiple(*lambdas_criterios):
    def validar(objeto):
        return all(
            criterio(objeto)
            for criterio in lambdas_criterios
        )

    return validar


validador = crear_validador_múltiple(
    lambda x: x > 10,
    lambda x: x < 100,
    lambda x: x % 2 == 0
)

print(validador(20))
print(validador(15))
print(validador(120))