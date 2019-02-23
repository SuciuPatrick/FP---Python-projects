def is_prime(number): #3
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    d = 3
    while d * d <= number:
        if number % d == 0:
            return False
    return True

def prime_numbers_list(list_numbers): #3
    new_list = []

    for x in list_numbers:
        if is_prime(x):
            new_list.append(x)
    return new_list

def print_prime_numbers(list_numbers): #3
    new_list = prime_numbers_list(list_numbers)
    print (new_list)

def add_list(l, number): #1
    l.append(number)

def print_list(list_numbers): #2
    print (list_numbers)

def panel_ui():
    list_numbers = []

    print ("1 = Add Number Into List")
    print("2 = Print List")
    print("3 = Print Prime Numbers")
    print("X = Exit")

    test = {
    'patrick': print_list(list_numbers)
    }

    #print (test['patrick'])
'''
    dictionar = {'1':print("ok"),
            2: print_list(list_numbers),
            3: print_prime_numbers(list_numbers),
            4: print("mata")
            }'''


def run():
    while True:
        start = input('->Press y/n: ')
        if start == 'y':
            panel_ui()
        elif start == 'n':
            return
        else:
            print ('Invalid command!')
run()
