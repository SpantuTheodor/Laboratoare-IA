import random


n = 6
m = 6
x_next = [-1, 0, 1, 0]  # sus, dreapta, jos, stanga
y_next = [0, 1, 0, -1]
queue = []


def Initialize(xs, ys, xf, yf):
    queue.append((xs, ys))
    return [xs, ys, xf, yf, xs, ys]


def isSafe(queue, matrix, state, x_next, y_next, solutie):
    if 0 <= state[4] + x_next < n and 0 <= state[5] + y_next < m:
        if solutie[state[4] + x_next][state[5] + y_next] == 0:
            if matrix[state[4] + x_next][state[5] + y_next] == 0:
                if (state[4] + x_next, state[5] + y_next) not in queue:
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


def transition(queue, matrix, state, solutie):
    min_counter = 0
    for index in range (len(queue) - 1 ) :
       if queue[index][2] == queue[0][2] :
           min_counter += 1
    if min_counter > 1 :
        random_number = random.randint( 0, min_counter - 1 )
    else :
        random_number = 0
    state[4] = queue[random_number][0]
    state[5] = queue[random_number][1]
    queue.pop(0)
    solutie[state[4]][state[5]] = 1
    print(state[4], state[5])
    if isFinal(state):
        print_function(state, matrix, solutie)
        return True
    for index in range(len(x_next)):
        if isSafe(queue, matrix, state, x_next[index], y_next[index], solutie):
            queue.append((state[4] + x_next[index], state[5] + y_next[index], abs( state[2]-state[4] + x_next[index] ) + abs( state[3]-state[5] + y_next[index] )))
        queue.sort(key=lambda x:x[2])
        print(queue)
    if transition(queue, matrix, state, solutie):
        return True
    solutie[state[4]][state[5]] = 0
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
    print(transition(queue, matrix, my_list, solutie))
