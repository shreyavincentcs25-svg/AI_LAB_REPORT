def simple_reflex_agent(room_a, room_b, position):
    print("\n--- SIMPLE REFLEX AGENT ---")

    rooms = {
        "A": room_a,
        "B": room_b
    }

    while True:
        print("Vacuum is in Room", position)

        if rooms[position] == "D":
            print("Action: SUCK")
            rooms[position] = "C"

        elif position == "A":
            print("Action: MOVE RIGHT")
            position = "B"

        elif position == "B":
            print("Action: MOVE LEFT")
            position = "A"

        if rooms["A"] == "C" and rooms["B"] == "C":
            print("Both rooms are clean.")
            print("Action: STOP")
            break


def goal_based_agent(room_a, room_b, position):
    print("\n--- GOAL BASED AGENT ---")

    rooms = {
        "A": room_a,
        "B": room_b
    }

    goal = {
        "A": "C",
        "B": "C"
    }

    while rooms != goal:
        print("Vacuum is in Room", position)

        if rooms[position] == "D":
            print("Action: SUCK")
            rooms[position] = "C"

        elif position == "A" and rooms["B"] == "D":
            print("Goal requires Room B to be cleaned.")
            print("Action: MOVE RIGHT")
            position = "B"

        elif position == "B" and rooms["A"] == "D":
            print("Goal requires Room A to be cleaned.")
            print("Action: MOVE LEFT")
            position = "A"

        else:
            break

    print("Final State:")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Goal achieved: Both rooms are clean.")


print("VACUUM CLEANER AGENT")

room_a = input("Enter status of Room A (D/C): ").upper()
room_b = input("Enter status of Room B (D/C): ").upper()

while room_a not in ["D", "C"] or room_b not in ["D", "C"]:
    print("Enter only D for Dirty or C for Clean.")
    room_a = input("Enter status of Room A (D/C): ").upper()
    room_b = input("Enter status of Room B (D/C): ").upper()

position = input("Enter starting position (A/B): ").upper()

while position not in ["A", "B"]:
    position = input("Enter starting position (A/B): ").upper()

print("\nInitial State:")
print("Room A:", room_a)
print("Room B:", room_b)
print("Vacuum Position:", position)

simple_reflex_agent(room_a, room_b, position)

goal_based_agent(room_a, room_b, position)