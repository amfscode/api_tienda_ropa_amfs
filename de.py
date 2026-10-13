def evaluar_afd(cadena: str) -> bool:
    """
    Simula el comportamiento del AFD expuesto en el diagrama.
    Retorna True si la cadena es aceptada, False en caso contrario.
    """
    # Configuración del autómata
    estado_actual = 1
    estados_aceptacion = {3}

    # Definición de la función de transición delta: (estado_actual, simbolo) -> siguiente_estado
    transiciones = {
        (1, '0'): 2,
        (2, '0'): 1,
        (2, '1'): 3,
        (3, '0'): 2,
        (3, '1'): 3  # Transición en bucle según el diagrama
    }

    print(f"--- Evaluando cadena: '{cadena}' ---")
    print(f"Estado inicial: q{estado_actual}")

    for paso, simbolo in enumerate(cadena, start=1):
        # Validar alfabeto
        if simbolo not in ('0', '1'):
            print(f"Error: El carácter '{simbolo}' no pertenece al alfabeto {{0, 1}}.")
            return False

        # Transición de estado
        clave = (estado_actual, simbolo)
        if clave in transiciones:
            estado_siguiente = transiciones[clave]
            print(f"Paso {paso}: Lee '{simbolo}' -> Transición q{estado_actual} a q{estado_siguiente}")
            estado_actual = estado_siguiente
        else:
            print(f"Paso {paso}: Lee '{simbolo}' -> Sin transición definida desde q{estado_actual}. Cadena RECHAZADA.")
            return False

    # Evaluación del estado final
    es_valida = estado_actual in estados_aceptacion
    if es_valida:
        print(f"Resultado: Cadena ACEPTADA (Estado final: q{estado_actual})\n")
    else:
        print(f"Resultado: Cadena RECHAZADA (Estado final: q{estado_actual} no es de aceptación)\n")

    return es_valida


# ==========================================
# Pruebas del programa
# ==========================================
if __name__ == "__main__":
    cadenas_de_prueba = ["01", "0101", "011", "011011", "1001"]

    for cadena in cadenas_de_prueba:
        evaluar_afd(cadena)