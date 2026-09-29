def componer_dos(f, g):
    def composicion(x):
        return f(g(x))

    return composicion


duplicar = lambda x: x * 2
sumar_tres = lambda x: x + 3

operacion = componer_dos(duplicar, sumar_tres)

print(operacion(5))