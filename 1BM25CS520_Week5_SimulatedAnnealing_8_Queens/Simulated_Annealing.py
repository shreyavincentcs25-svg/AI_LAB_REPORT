import random
import math

def calculate_cost(board):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def print_board(board):
    for row in range(8):
        for col in range(8):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


def simulated_annealing():
    board = [random.randint(0, 7) for _ in range(8)]

    temperature = 100
    alpha = 0.99
    current_cost = calculate_cost(board)
    steps = 0

    print("\n" + "=" * 45)
    print("       8-QUEENS SIMULATED ANNEALING")
    print("=" * 45)

    print("\nInitial Board:")
    print_board(board)
    print("\nInitial Cost:", current_cost)

    while temperature > 0.01 and current_cost != 0:

        new_board = board.copy()
        col = random.randint(0, 7)
        row = random.randint(0, 7)

        new_board[col] = row

        neighbour_cost = calculate_cost(new_board)
        delta = current_cost - neighbour_cost

        if delta > 0:
            board = new_board
            current_cost = neighbour_cost

        else:
            probability = math.exp(delta / temperature)
            r = random.random()

            if r < probability:
                board = new_board
                current_cost = neighbour_cost

        temperature = alpha * temperature
        steps += 1

        if steps % 100 == 0 or current_cost == 0:
            print("\nStep:", steps)
            print("Temperature:", round(temperature, 4))
            print("Current Cost:", current_cost)

    print("\n" + "=" * 45)

    if current_cost == 0:
        print("          SOLUTION FOUND")
    else:
        print("       SOLUTION NOT FOUND")

    print("=" * 45)

    print("\nFinal Chessboard:")
    print_board(board)

    print("\nFinal Cost:", current_cost)
    print("Total Steps:", steps)



simulated_annealing()