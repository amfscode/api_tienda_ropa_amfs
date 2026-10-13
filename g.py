def automata(cadena):
    estado = 1

    for simbolo in cadena:

        if estado == 1:
            if simbolo == "0" or simbolo == "1":
                estado = 2
            else:
                return False

        elif estado == 2:
            if simbolo == "0":
                estado = 3
            elif simbolo == "1":
                estado = 2
            else:
                return False

        elif estado == 3:
            if simbolo == "0":
                estado = 3
            elif simbolo == "1":
                estado = 2
            else:
                return False

    return estado == 3


cadena = input("Ingrese una cadena binaria: ")

if automata(cadena):
    print("Cadena aceptada")
else:
    print("Cadena rechazada")