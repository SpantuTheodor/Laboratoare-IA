queue = [(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (3, 6)]
colors = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
neighbors = [(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (3, 6)]


def remove_consistent_value(auxiliary, colors):
    okay = False
    for i in colors[auxiliary[0] - 1]:
        okay = False
        for j in colors[auxiliary[1] - 1]:
            if j != i:
                okay = True
        if not okay:
            colors[auxiliary[0]].remove(i)
    return okay


def ac_3(queue, colors):
    while len(queue) != 0:
        auxiliary = queue[0]
        queue.pop(0)
        print(queue)
        if not remove_consistent_value(auxiliary, colors):
            for i in neighbors:
                if i[0] == auxiliary[0]:
                    queue.append((i[1], auxiliary[0]))

    if len(queue) == 0:
        print("gata")


ac_3(queue, colors)
