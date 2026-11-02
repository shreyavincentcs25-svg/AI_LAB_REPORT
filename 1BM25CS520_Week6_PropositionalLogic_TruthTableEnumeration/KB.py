from itertools import product


def implies(p, q):
    return (not p) or q


def evaluate_kb(model):
    P = model["P"]
    Q = model["Q"]
    R = model["R"]

    sentence1 = implies(Q, P)
    sentence2 = implies(P, not Q)
    sentence3 = Q or R

    return sentence1 and sentence2 and sentence3


def evaluate_query(model, query):
    P = model["P"]
    Q = model["Q"]
    R = model["R"]

    if query == "R":
        return R

    if query == "R -> P":
        return implies(R, P)

    if query == "Q -> R":
        return implies(Q, R)


def tt_entails(query):

    symbols = ["P", "Q", "R"]

    for values in product([False, True], repeat=3):

        model = dict(zip(symbols, values))

        kb_true = evaluate_kb(model)

        if kb_true:
            if not evaluate_query(model, query):
                return False

    return True


queries = ["R", "R -> P", "Q -> R"]

for query in queries:
    print(query, ":", tt_entails(query))