n = 6
m = 6
x_next = [-1,0,1,0] # sus, dreapta, jos, stanga
y_next = [0,1,0,-1]


def Initialize(xs, ys, xf, yf):
    return [xs, ys, xf, yf, xs, ys]

def isSafe(matrix, state, x_next, y_next, solutie):
    if 0 <= state[4] + x_next < n and 0 <= state[5] + y_next < m:
        if solutie[state[4] + x_next][state[5] + y_next] == 0:
            if matrix[state[4] + x_next][state[5] + y_next] == 0:
                return True
    return False

def isFinal(list):
    if list[4] == list[2] and list[5] == list[3]:
        return True
    return False


def print_function(state, matrix, solutie):
    solutie[state[0]][state[1]] = 's'
    solutie[state[4]][state[5]] = 'f'
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 :
                print("#", end = " ")
            else :
                print(solutie[i][j], end=" ")
        print()


def transition(matrix, state, solutie):
    if isFinal(state):
        print_function(state, matrix, solutie)
        return True
    for index in range(len(x_next)):
        if isSafe(matrix, state, x_next[index], y_next[index], solutie):
            state[4] = state[4] + x_next[index]
            state[5] = state[5] + y_next[index]
            solutie[state[4]][state[5]] = 1
            print(state[4], state[5])
            if transition(matrix, state, solutie):
                return True
            solutie[state[4]][state[5]] = 0
            state[4] = state[4] - x_next[index]
            state[5] = state[5] - y_next[index]
    return False


if __name__ == '__main__':
    matrix = [[1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0]]
    solutie = [ [ 0 for j in range(n) ] for i in range(m) ]
    # xs = 1
    # ys = 2
    # xf = 4
    # yf = 3
    my_list = Initialize(1, 2, 4, 3)
    print(transition(matrix, my_list, solutie))
