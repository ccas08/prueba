def divisors(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return divisors


def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))
    print("termino mi programa")


if __name__ == "__main__":
    run()
