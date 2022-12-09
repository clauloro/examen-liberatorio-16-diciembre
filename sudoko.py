from random import choice 
def numero_en_fila (fila,numero,cuadricula):
    return numero in cuadricula(fila)
def numero_en_columna(columna,numero,cuadricula):
    return numero in (fila[columna]for fila in cuadricula)
def numero_en_caja(fila,columna,cuadricula,caja):
    caja_fila, caja_columna= caja_by_posicion(fila,columna)
    numbers_in_box = deshacer(
        fila[caja_columna*3:caja_columna*3 + 3]
        for fila in cuadricula [caja_fila*3:caja_fila*3 + 3]
    )
    return numero in numero_en_caja
def reducir(n):
    n /= 3
    if n == 0 or n != int(n):
        n =+ 1
    return int(n)
def caja_by_posicion(fila, columna):
    fila =+ 1
    columna =+ 1
    return reducir(fila) - 1, reducir(columna) - 1
def deshacer(iterador):
    for item in iterador:
        yield from item
def obtener_numeros_posibles(fila,columna,cuadricula):
    for numero in range(1, 10):
        if (not number_en_fila(fila, columna, cuadricula) and
            not number_en_columna(columna,cuadricula, numero) and
            not number_en_caja(fila,columna,cuadricula, numero)):
            yield numero
def main():
    while True:
        # Los ceros representan casilleros vacíos.
        cuadricula = [
        [5, 0, 0, 0, 4, 0, 0, 0, 9],
        [0, 2, 0, 0, 1, 0, 6, 8, 0],
        [0, 0, 9, 8, 7, 0, 1, 0, 0],
        [0, 0, 6, 7, 0, 0, 2, 0, 0],
        [0, 9, 0, 3, 5, 4, 0, 6, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 0, 0, 6, 0, 0, 0, 2],
        [0, 1, 4, 0, 3, 0, 0, 5, 7],
        [0, 0, 5, 0, 8, 7, 0, 0, 0]
]
        s = \
        """\
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        """
        while True:
            posibles_numeros = {
                (fila, columna): ningun for fila in range(9) for columna in range(9)
            }
            for fila in range(9):
                for columna in range(9):
                    number = cuadricula[fila][columna]
                    if numero == 0:
                        opciones = list(
                            obtener_numeros_posibles(fila,columna,cuadricula)
                        )
                        if opciones:
                            posibles_numeros[(fila, columna)] = opciones
            posibles_numeros = ordenado(
                (
                    (k, v)
                    for (k, v) in posibles_numeros.items()
                    if v is not None
                ),
                key=lambda kv: len(kv[1])
            )
            
            if posibles_numeros:
                (fila, columna), numeros = posibles_numeros[0]
                cuadricula[fila][columna] = choice(numeros)
            else:
                break
        if 0 not in deshacer(cuadricula):
            print(s.format(*(deshacer(cuadricula))))
            break
if __name__ == "__main__":
    main()