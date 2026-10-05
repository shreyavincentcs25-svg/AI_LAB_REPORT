import heapq

def misplaced(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join("_" if x == 0 else str(x)
                       for x in state[i:i+3]))
    print()


def a_star(initial, goal):

    open_list = []

    g = 0
    h = misplaced(initial, goal)
    f = g + h

    heapq.heappush(open_list, (f, g, initial))

    parent = {initial: None}
    cost = {initial: 0}

    while open_list:

        f, g, current = heapq.heappop(open_list)

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Solution Path\n")

            for step, state in enumerate(path):

                g_value = step
                h_value = misplaced(state, goal)
                f_value = g_value + h_value

                print("Step", step)
                print_state(state)

                print("g(n) =", g_value)
                print("h(n) =", h_value)
                print("f(n) =", f_value)
                print("--------------------")

            print("Number of moves:", len(path) - 1)
            return

        for neighbor in get_neighbors(current):

            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:

                cost[neighbor] = new_g

                h = misplaced(neighbor, goal)
                f = new_g + h

                parent[neighbor] = current

                heapq.heappush(
                    open_list,
                    (f, new_g, neighbor)
                )

    print("No solution")


initial = (
    2, 8, 3,
    1, 6, 4,
    0, 7, 5
)

goal = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)

a_star(initial, goal)