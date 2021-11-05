"""def run():
    squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i ** 2)
    print(squares)"""  # funcion normal


def eleva_al_2(i):
    return i ** 2


def run():
    squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]

    ones = [1 for i in range(5)]
    # [1, 1, 1, 1, 1]
    squares2 = [eleva_al_2(i) for i in range(5)]
    # [0, 1, 4, 9, 16]
    print(squares, " ", ones, " ", squares2)


def eleva_al_2(i):
    return i ** 2


cuadrados = [eleva_al_2(i) for i in range(5)]
# [0, 1, 4, 9, 16]
if __name__ == "__main__":
    run()
