def acepta(cadena):
    transiciones = {
        "q1": {"0": "q2", "1": "q2"},
        "q2": {"0": "q3", "1": "q2"},
        "q3": {"0": "q3", "1": "q2"},
    }

    estado = "q1"

    for simbolo in cadena:
        if simbolo not in "01":
            return False
        estado = transiciones[estado][simbolo]

    return estado == "q3"


for cadena in ["011", "0110", "10", "0"]:
    print(cadena, "Aceptada" if acepta(cadena) else "Rechazada")