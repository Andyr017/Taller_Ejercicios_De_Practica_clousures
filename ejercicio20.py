def crear_consultor(campo):
    def consultar(lista, criterio):
        return list(
            filter(
                lambda objeto: criterio(objeto[campo]),
                lista
            )
        )

    return consultar


productos = [
    {"nombre": "Laptop", "precio": 800},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 50},
    {"nombre": "Monitor", "precio": 300}
]

consultar_precio = crear_consultor("precio")

resultado = consultar_precio(
    productos,
    lambda precio: precio > 100
)

print(resultado)