palindromo = lambda string: string == string[::-1]

print(palindromo("ana"))

"""filter"""
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = list(filter(lambda x: x % 2 != 0, my_list))
print(odd)

"""map"""
my_list2 = [1, 2, 3, 4, 5]
squares2 = list(map(lambda x: x ** 2, my_list))
print(squares2)
