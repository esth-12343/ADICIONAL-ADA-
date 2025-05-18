def leer_movil(lines):
    pi, di, pd, dd = map(int, lines.pop(0).split())

    if pi == 0:
        peso_i, balanceado_i = leer_movil(lines)
    else:
        peso_i = pi
        balanceado_i = True

    if pd == 0:
        peso_d, balanceado_d = leer_movil(lines)
    else:
        peso_d = pd
        balanceado_d = True

    esta_balanceado = (peso_i * di == peso_d * dd) and balanceado_i and balanceado_d
    peso_total = peso_i + peso_d

    return peso_total, esta_balanceado


def procesar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo if linea.strip()]

    i = 0
    while i < len(lineas):
        if lineas[i] == "0 0 0 0":
            break

        def contar_lineas(idx):
            pi, _, pd, _ = map(int, lineas[idx].split())
            total = 1
            if pi == 0:
                total += contar_lineas(idx + total)
            if pd == 0:
                total += contar_lineas(idx + total)
            return total

        total_lineas = contar_lineas(i)
        bloque = lineas[i:i+total_lineas]
        copia_bloque = bloque.copy()

        _, balanceado = leer_movil(copia_bloque)
        print("ST" if balanceado else "NO")  #  "ST" y "NO"

        i += total_lineas


procesar_archivo("entrada.txt")print("Hola desde mi script")
