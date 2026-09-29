def crear_conversor(tasa, margen_lambda):
    def convertir(monto):
        conversion = monto * tasa
        margen = margen_lambda(monto, tasa)

        return conversion + margen

    return convertir


margen = lambda monto, tasa: monto * tasa * 0.02

conversor = crear_conversor(1.10, margen)

print(conversor(100))