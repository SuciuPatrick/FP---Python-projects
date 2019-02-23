'''
[11] The palindrome of a number is the number obtained by reversing the
order of digits. E.g. palindrome (237) = 732). For a given natural number n,
determine its palindrome.

'''
def reverseNumber(nr):
    '''
    This function return the reverse of a number
    input- integer
    output- integer
    '''
    rev = 0

    while (nr):
        rev = rev * 10 + nr % 10
        nr //=10
    return rev

def printNumber(nr):
    print("Inversul numarului este: " +  str(nr))

def reverseTests():
    assert reverseNumber(123)==321
    assert reverseNumber(53214)==41235
    assert reverseNumber(65432)==23456
    assert reverseNumber(9)==9
    assert reverseNumber(1111)==1111

def ui_homework():
    while True:
        try:
            nr = input('Insert Number->')
            nr = int(nr)
            if (nr < 0):
                print("enter a positive number.")
            else:
                resolve = reverseNumber(nr)
                printNumber(resolve)
            return
        except ValueError as ve:
            print ("Illegal integer value given!")
        

def run():
    while True:
        x = input('Press y/n: ')
        if x == 'y':
            ui_homework()
        elif x == 'n':
            return
        else:
            print('invalid command()')

reverseTests()
run()
