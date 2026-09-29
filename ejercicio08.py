def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []

    def agregar(valor):
        nonlocal datos

        if filtro_ruido_lambda(valor):
            datos.append(valor)

        if len(datos) == 0:
            return 0

        return sum(datos) / len(datos)

    return agregar


filtro = lambda valor: 10 <= valor <= 100

promediador = crear_promediador_filtrado(filtro)

print(promediador(20))
print(promediador(30))
print(promediador(150))
print(promediador(40))