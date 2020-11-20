# functia de evaluare euristica: F = sum(dyc) - sum(dyo)

def calcul_functie_euristica(om, calculator):
    sum = 0
    for coord in calculator:
        sum += coord[0]
    for coord in om:
        sum -= 3 - coord[0]
    return sum


def is_final(matrix):
    for i in range(len(matrix[0])):
        if matrix[0][i] != 'o':
            return False
    for i in range(len(matrix[3])):
        if matrix[3][i] != 'c':
            return False
    return True


def is_valid(x, y, matrix):
    if 0 <= x <= 3 and 0 <= y <= 3 and matrix[x][y] != 'c' and matrix[x][y] != 'o':
        return True
    return False


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()


def simulate_computer_move(om, calculator, matrix, nivel, euristica):
    # jos, sus, dreapta, stanga, diagonale
    xc = [1, -1, 0, 0, 1, -1, 1, -1]
    yc = [0, 0, 1, -1, 1, -1, -1, 1]

    if nivel == 1:

        euristice_minime = []
        noduri_euristice_minime = []
        aux = []
        euristica = None
        for i in range(len(calculator)):  # nr pieselor
            for j in range(len(xc)):
                if is_valid(calculator[i][0] + xc[j], calculator[i][1] + yc[j], matrix):
                    matrix[calculator[i][0]][calculator[i][1]] = 0
                    calculator[i][0] += xc[j]
                    calculator[i][1] += yc[j]
                    matrix[calculator[i][0]][calculator[i][1]] = 'c'

                    if simulate_computer_move(om, calculator, matrix, 2, euristica) is not False:
                        euristica_minima, nod_euristica_minima1, nod_euristica_minima2 = simulate_computer_move(om, calculator, matrix, 2, euristica)
                    if euristica is None or euristica <= euristica_minima:
                        euristica = euristica_minima

                    nod_euristica_minima = [nod_euristica_minima1, nod_euristica_minima2]
                    euristice_minime.append(euristica_minima)
                    noduri_euristice_minime.append(nod_euristica_minima)
                    aux.append([calculator[i][0], calculator[i][1]])

                    calculator[i][0] -= xc[j]
                    calculator[i][1] -= yc[j]
                    matrix[calculator[i][0] + xc[j]][calculator[i][1] + yc[j]] = 0
                    matrix[calculator[i][0]][calculator[i][1]] = 'c'

        euristica_maxima = max(euristice_minime)
        nod_euristica_maxima = noduri_euristice_minime[euristice_minime.index(max(euristice_minime))]
        nod_auxiliar = aux[euristice_minime.index(min(euristice_minime))]
        nod_euristica_maxima.append(nod_auxiliar)
        return euristica_maxima, nod_euristica_maxima

    elif nivel == 2:

        euristice_maxime = []
        noduri_euristice_maxime = []
        euristica = None
        aux = []
        for i in range(len(om)):  # nr pieselor
            for j in range(len(xc)):
                if is_valid(om[i][0] + xc[j], om[i][1] + yc[j], matrix):
                    matrix[om[i][0]][om[i][1]] = 0
                    om[i][0] += xc[j]
                    om[i][1] += yc[j]
                    matrix[om[i][0]][om[i][1]] = 'o'

                    if simulate_computer_move(om, calculator, matrix, 3, euristica) is not False:
                        euristica_maxima, nod_euristica_maxima = simulate_computer_move(om, calculator, matrix, 3, euristica)
                    if euristica is None or euristica >= euristica_maxima:
                        euristica = euristica_maxima

                    euristice_maxime.append(euristica_maxima)
                    noduri_euristice_maxime.append(nod_euristica_maxima)
                    aux.append([om[i][0], om[i][1]])

                    om[i][0] -= xc[j]
                    om[i][1] -= yc[j]
                    matrix[om[i][0] + xc[j]][om[i][1] + yc[j]] = 0
                    matrix[om[i][0]][om[i][1]] = 'o'

        euristica_minima = min(euristice_maxime)
        nod_euristica_minima = noduri_euristice_maxime[euristice_maxime.index(min(euristice_maxime))]
        nod_auxiliar = aux[euristice_maxime.index(min(euristice_maxime))]

        if euristica is None or euristica_minima >= euristica:
            return euristica_minima, nod_euristica_minima, nod_auxiliar
        return False

    elif nivel == 3:

        euristice_maxime = []
        noduri_euristice_maxime = []
        nod = list()

        for i in range(len(calculator)):  # nr pieselor
            maxim = -99999

            for j in range(len(xc)):
                if is_valid(calculator[i][0] + xc[j], calculator[i][1] + yc[j], matrix):

                    # Pas inainte
                    matrix[calculator[i][0]][calculator[i][1]] = 0
                    calculator[i][0] += xc[j]
                    calculator[i][1] += yc[j]
                    matrix[calculator[i][0]][calculator[i][1]] = 'c'

                    # Verificare maxim
                    calcul = calcul_functie_euristica(om, calculator)
                    if calcul > maxim:
                        maxim = calcul
                        nod_i = calculator[i][0]
                        nod_j = calculator[i][1]

                    print("Nod_verificat", calculator[i])
                    print("Calcul_euristica:", calcul)
                    print("Matrice:")
                    print_matrix(matrix)

                    # Pas Inapoi
                    calculator[i][0] -= xc[j]
                    calculator[i][1] -= yc[j]
                    matrix[calculator[i][0] + xc[j]][calculator[i][1] + yc[j]] = 0
                    matrix[calculator[i][0]][calculator[i][1]] = 'c'
                    print()

            if nod is not None:
                euristice_maxime.append(maxim)
                noduri_euristice_maxime.append([nod_i, nod_j])
                euristica_maxima = max(euristice_maxime)
                index = euristice_maxime.index(max(euristice_maxime))
                nod_euristica_maxima = noduri_euristice_maxime[index]

        if euristica is None or euristica_maxima <= euristica:
            return euristica_maxima, nod_euristica_maxima
        return False


init = [['c', 'c', 'c', 'c'],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ['o', 'o', 'o', 'o']]
om = [[3, 0], [3, 1], [3, 2], [3, 3]]
calculator = [[0, 0], [0, 1], [0, 2], [0, 3]]
result1, result2 = simulate_computer_move(om, calculator, init, 1, None)

print("Euristica_maxima: ", result1)
print("Mutari_facute: ", result2)
