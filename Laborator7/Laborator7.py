import random
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
yd = [0, 0, 0, 1]
err_patratica = 1
aux_y5 = [0, 0, 0, 0]
aux_err = [0, 0, 0, 0]

w13 = random.uniform(0, 1)
w14 = random.uniform(0, 1)
w23 = random.uniform(0, 1)
w24 = random.uniform(0, 1)
w35 = random.uniform(0, 1)
w45 = random.uniform(0, 1)

theta3 = random.uniform(0, 1)
theta4 = random.uniform(0, 1)
theta5 = random.uniform(0, 1)
while err_patratica > 0.001:
    for index in range(len(x1)):
        # Iesirile neuronilor din stratul ascuns
        y3 = sigmoid(x1[index] * w13 + x2[index] * w23 + theta3)
        y4 = sigmoid(x1[index] * w14 + x2[index] * w24 + theta4)
        # print()
        # print("Iesirea neuronilor din stratul ascuns : ")
        # print(y3)
        # print(y4)

        # Iesirile neuronilor din stratul de iesire
        y5 = sigmoid(y3 * w35 + y4 * w45 + theta5)
        aux_y5[index] = y5
        err = yd[index] - y5
        aux_err[index] = err
        err_patratica += err
        delta5 = y5 * (1 - y5) * err
        # print()
        # print("Iesirea neuronilor din stratul de iesire : ", y5)
        # print("Eroarea : ", err)
        # print("Gradient : ", delta5)

        # Corectiile ponderilor si a pragului stratului de iesire
        alfa = 0.1
        deltaw35 = alfa * y3 * delta5
        deltaw45 = alfa * y4 * delta5
        deltatheta5 = alfa * (-1) * delta5
        # print()
        # print("Corectiile ponderilor si a pragului stratului de iesire : ")
        # print(deltaw35)
        # print(deltaw45)
        # print(deltatheta5)

        # Gradientii de eroare pentru neuronii 3 si 4 din stratul ascuns
        delta3 = y3 * (1 - y3) * delta5 * w35
        delta4 = y4 * (1 - y4) * delta5 * w45
        # print()
        # print("Gradientii de eroare pentru neuronii 3 si 4 din stratul ascuns : ")
        # print(delta3)
        # print(delta4)

        # Corectiile ponderilor si a pragului stratului ascuns
        deltaw13 = alfa * x1[index] * delta3
        deltaw23 = alfa * x2[index] * delta3
        deltatheta3 = alfa * (-1) * delta3
        deltaw14 = alfa * x1[index] * delta4
        deltaw24 = alfa * x2[index] * delta4
        deltatheta4 = alfa * (-1) * delta4
        # print()
        # print("Corectiile ponderilor si a pragului stratului ascuns : ")
        # print(deltaw13)
        # print(deltaw23)
        # print(deltatheta3)
        # print(deltaw14)
        # print(deltaw24)
        # print(deltatheta4)

        # Actualizarea ponderilor si a pragurilor
        w13 = w13 + deltaw13
        w14 = w14 + deltaw14
        w23 = w23 + deltaw23
        w24 = w24 + deltaw24
        w35 = w35 + deltaw35
        w45 = w45 + deltaw45
        theta3 = theta3 + deltatheta3
        theta4 = theta4 + deltatheta4
        theta5 = theta5 + deltatheta5

        # print()
        # print("Actualizarea ponderilor si a pragurilor : ")
        # print(w13)
        # print(w14)
        # print(w23)
        # print(w24)
        # print(w35)
        # print(w45)
        # print(theta3)
        # print(theta4)
        # print(theta5)

    err_patratica = 1 / 4 * err_patratica ** 2
    print(err_patratica)
print("Iesire dorita : ", yd)
print("Iesire reala : ", aux_y5)
print("Erori : ", aux_err)
print("Suma erori patratice : ", err_patratica)
