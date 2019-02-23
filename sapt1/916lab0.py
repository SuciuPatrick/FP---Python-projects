def is_prime(x):
    '''
    Function that checks whether an integer x is prima or not 
    input:x - integer
    preconditions: -
    output: r - boolean
    postconditions: r = True if x is prime
                        False otherwise
    '''
    if x < 2:
        return False
    if x==2:
        return True
    if x % 2 == 0:
        return False
    d=3
    #it is enough to check for divisors till the squared root
    while d*d<=x:
        if x % d == 0:
            return False
        d+=2
    return True

def test_is_prime():
    assert is_prime(25)==False
    assert is_prime(-3)==False
    assert is_prime(0)==False
    assert is_prime(1)==False
    assert is_prime(2)==True
    assert is_prime(3)==True
    assert is_prime(4)==False
    assert is_prime(7)==True
    assert is_prime(21)==False

def print_is_prime(x,r):
    if r:
        print(str(x)+" is prime")
    else:
        print(str(x)+" is not prime")

def ui_prime():
    while True:
        try:
            x = input("Insert an integer:")
            x = int(x)
            r = is_prime(x)
            print_is_prime(x,r)
            return
        except ValueError as ve:
            print("Illegal integer value given!")

def run():
    while True:
        x = input(">>")
        if x=="exit":
            return
        elif x=="prime":
            ui_prime()
        else:
            print("Invalid command!")
        
test_is_prime()
run()
