def largestNumber(nr):
    '''
    This function returns  the largest number that can be formed with the digits of
    number.
    input: nr - integer
    output: rez - integer
    
    '''
    frecv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while nr != 0:
        frecv[nr % 10] += 1
        nr //= 10
    #frecv.sort(reverse=True)
    rez = 0
    i = 9
    while i >= 0:
        while frecv[i] != 0:
            rez = rez * 10 + i
            frecv[i] -= 1
        i -= 1
    return rez

def printNumber(nr):
    print(nr)

def testLargestNumber():
    assert largestNumber(1234)==4321
    assert largestNumber(123456789)==987654321
    assert largestNumber(321)==321
    assert largestNumber(0)==0
    assert largestNumber(51326)==65321
    assert largestNumber(678)==876
    
        
def ui_homework():
    while True:
        try:
            var = input('insert an integer: ')
            var = int(var)
            if (var < 0):
                print ("Sorry, you must enter a positive number")
            else:
                resolve = largestNumber(var)
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

testLargestNumber()
run()
