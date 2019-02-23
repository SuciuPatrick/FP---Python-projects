def reverseNumber(nr):
    rev = 0

    while (nr):
        rev = rev * 10 + nr % 10
        nr //= 10
    return rev

def printNumber(rev):
    print(rev)

def ui_homework():
    while True:
        try:
            var = input('insert an integer: ')
            var = int(var)
            if (var < 0):
                print ("Sorry, you must enter a positive number")
            else:
                resolve = reverseNumber(var)
                printNumber(resolve)
            return
        except ValueError as ve:
            print("Illegal integer value given!")

def run():
    while True:
        x = input("->Press y/n : ")
        if x == 'n':
            return
        elif x == 'y':
            ui_homework()
        else:
            print('invalid command()')

run()
        
