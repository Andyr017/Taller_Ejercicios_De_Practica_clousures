def crear_sistema_eventos():
    suscriptores = {}

    def gestionar(accion, evento=None, fn=None):
        if accion == "suscribir":
            if evento not in suscriptores:
                suscriptores[evento] = []

            suscriptores[evento].append(fn)

        elif accion == "emitir":
            if evento in suscriptores:
                for suscriptor in suscriptores[evento]:
                    suscriptor()

    return gestionar


sistema = crear_sistema_eventos()

sistema(
    "suscribir",
    "mensaje",
    lambda: print("Suscriptor 1 recibió el evento")
)

sistema(
    "suscribir",
    "mensaje",
    lambda: print("Suscriptor 2 recibió el evento")
)

sistema("emitir", "mensaje")