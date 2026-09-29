def crear_descuento_dinamico(regla_condicional_lambda):
    def calcular(precio):
        if regla_condicional_lambda(precio):
            return precio * 0.90

        return precio

    return calcular


regla = lambda precio: precio > 100

descuento = crear_descuento_dinamico(regla)

print(descuento(150))
print(descuento(80))