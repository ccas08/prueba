def run():
    my_dict = {o: i ** 3 for i in range(1, 101) if 1 % 3 != 0}
    print(my_dict)


"""def run():

    my_dict = {i : round(i**0.5,2) for i in  range(1,1001)}

    print(my_dict)

if __name__=='__main__':
    run()"""  # reto


if __name__ == "__main__":
    run()
