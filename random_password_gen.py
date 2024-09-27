import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '?', '.', ',', '#', '+', '%']


def random_pin():
    amount_let = int(input("How many letters would you like? "))
    amount_nums = int(input("How many numbers would you like? "))
    amount_symbols = int(input("How many symbols would you like? "))

    lst_let = [random.choice(letters) for i in range(amount_let)]
    lst_nums = [random.choice(nums) for i in range(amount_nums)]
    lst_symbols = [random.choice(symbols) for i in range(amount_symbols)]

    password = lst_let + lst_nums + lst_symbols  # merge lists

    random.shuffle(password)  # shuffle the list
    str_password = ''.join(password)  # turns list to a string???
    return str_password


print(random_pin())