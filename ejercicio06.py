def crear_contador_paso(fn_paso):
    cuenta = 0

    def incrementar():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)

        return cuenta

    return incrementar


paso = lambda cuenta: cuenta + 5

contador = crear_contador_paso(paso)

print(contador())
print(contador())
print(contador())