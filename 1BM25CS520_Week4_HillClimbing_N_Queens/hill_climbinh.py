import random

def calculate_cost(board):
    conflicts = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def print_board(board):
    for row in range(4):
        for col in range(4):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


def hill_climbing():
    board = [random.randint(0, 3) for _ in range(4)]
    current_cost = calculate_cost(board)
    steps = 0

    print("\n" + "=" * 40)
    print("       4-QUEENS HILL CLIMBING")
    print("=" * 40)

    print("\nInitial Board:")
    print_board(board)
    print("\nInitial Cost:", current_cost)

    while current_cost != 0:
        neighbours = []

        for col in range(4):
            for row in range(4):
                if board[col] != row:
                    new_board = board.copy()
                    new_board[col] = row
                    cost = calculate_cost(new_board)
                    neighbours.append((cost, new_board))

        min_cost, best_board = min(neighbours, key=lambda x: x[0])

        if min_cost >= current_cost:
            print("\nLocal Minimum Reached!")
            print("No better neighbouring state found.")
            print("\nFinal Cost:", current_cost)
            print_board(board)
            return

        board = best_board
        current_cost = min_cost
        steps += 1

        print("\nStep", steps)
        print_board(board)
        print("Cost:", current_cost)

    print("\n" + "=" * 40)
    print("          GOAL STATE REACHED")
    print("=" * 40)

    print("\nFinal Solution:")
    print_board(board)
    print("\nFinal Cost:", current_cost)
    print("Total Steps:", steps)


hill_climbing()