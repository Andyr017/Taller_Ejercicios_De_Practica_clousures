def crear_conmutador(lista_estados):
    posicion = 0

    def cambiar():
        nonlocal posicion

        estado = lista_estados[posicion]
        posicion = (posicion + 1) % len(lista_estados)

        return estado

    return cambiar


conmutador = crear_conmutador(["BAJO", "MEDIO", "ALTO"])

print(conmutador())
print(conmutador())
print(conmutador())
print(conmutador())
print(conmutador())