'''
[1] Generate the first prime number larger than a given natural number n.
'''
def isPrime(nr):
        """
        This function is returning true of false if a number is prime or not.
        input- integer
        output- boolean
        """
        if (nr < 2):
                return False
        if nr == 2:
                return True
        if nr % 2 == 0:
                return False
        for d in range (3, nr, 2):
                if d * d <= nr and nr % d == 0:
                        return False
        return True

def nextPrimeNumber(nr):
        nr += 1
        while True:
                if isPrime(nr):
                        return nr
                nr += 1

def printNumber(nr):
        print("The number is: " + str(nr))

def testNextPrime():
        assert nextPrimeNumber(0)==2
        assert nextPrimeNumber(120)==127
        assert nextPrimeNumber(20)==23
        assert nextPrimeNumber(345)==347

def ui_homework():
    while True:
        try:
            var = input('insert an integer: ')
            var = int(var)
            if (var < 0):
                print ("Sorry, you must enter a positive number")
            else:
                resolve = nextPrimeNumber(var)
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

testNextPrime()
run()

