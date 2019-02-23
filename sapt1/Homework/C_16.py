'''

[16] Generate the largest perfect number smallest than a given natural
number n. If such a number does not exist, a message should be displayed.
A number is perfect if it is equal to the sum of its divisors,
except itself. E.g. 6 is a perfect number (6=1+2+3).
'''

def sumDivisors(nr):
    '''
    Returns the sum of divisors
    input-integer
    output-integer
    '''
    sumDiv = 1

    i = 2
    while i * i <= nr:
        if nr % i == 0:
            sumDiv += i;
            if i != nr // i:
                   sumDiv += nr // i
        i += 1

    return sumDiv

def perfectNumber(nr):
    '''
    Returns the next prime number larger than nr
    input-integer
    output-integer
    '''
    nr += 1
    while True:
        if sumDivisors(nr) == nr:
            return nr
        else:
            nr += 1
        
def printRez(nr):
	print(nr)

def testNextPrime():
    assert perfectNumber(2)==6
    assert perfectNumber(10)==28
    
def ui_homework():
    while True:
        try:
            var = input('insert an integer: ')
            var = int(var)
            if (var < 0):
                print ("Sorry, you must enter a positive number")
            else:
                resolve = perfectNumber(var)
                printRez(resolve)
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

testNextPrime()
run()
