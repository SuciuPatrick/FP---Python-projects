import math

# Setters and getters

def setSign(dictionar, sign):
    dictionar["sign"] = sign

def setReal(dictionar, real):
    dictionar["real"] = real

def setImaginary(dictionar, imaginary):
    dictionar["imaginary"] = imaginary
	
def printList(listOfComplexNumber):
    '''
    It prints all the number that are contained in the list
    '''
    for comp in listOfComplexNumber:
        print (comp["real"], comp["sign"], comp["imaginary"])

def printPartOfList(listOfComplexNumber, st, dr):
    '''
    It prints the elements from st to dr
    '''
    while st < dr:
        print (listOfComplexNumber[st]["real"], listOfComplexNumber[st]["sign"], listOfComplexNumber[st]["imaginary"])
        st += 1
        
def getReal(dictionar):
    return dictionar["real"]

def getImaginary(dictionar):
    return dictionar["imaginary"]

# End of setters and getters

def creationNumber(number):
    '''
Transforms the digits of the string of imaginary part into an integer
input - string
return - integer
    '''
    nr = 0
    for x in number:
       if x >= '0' and x <= '9':
               nr = nr * 10 + int(x)
    return nr

def testsCreation():
   assert creationNumber("123ghfda")==123
   assert creationNumber("asas421df")==421
   assert creationNumber("31i")==31
   assert creationNumber("20i")==20


def moduleOfNumbers(complexNumber):
   '''
return the module of a complex number
input - dictionary
return - float
   '''
   nr1 = int(getReal(complexNumber))
   nr2 = creationNumber(getImaginary(complexNumber))

   return math.sqrt(nr1 * nr1 + nr2 * nr2)

def moduleInterval(module):
    if module >= 0 and module <= 10:
        return True
    return False

def longestSeqModule(x):
    '''
    n = how many numbers we have
    We use st and dr to determine how long is the sequence in O(n)

    '''
    n = len(x)

    i = 1
    maxim = 0
    st = 0
    dr = 0
    while i < n:
        module1 = moduleOfNumbers(x[i])
        module2 = moduleOfNumbers(x[i - 1])
        if moduleInterval(module1) and moduleInterval(module2):
            j = i + 1
            if j < n:
                while moduleInterval(moduleOfNumbers(x[j])) and moduleInterval(moduleOfNumbers(x[j - 1])) and j < n - 1:
                   j += 1
                if j - i + 1 > maxim:
                    maxim = j - i + 1
                    st = i
                    dr = j
            i = j
        i += 1

    listOfStDr = []
    listOfStDr.append(st)
    listOfStDr.append(dr)
    return listOfStDr

def longestSeqReal(x):
    '''
    n = how many numbers we have
    We use st and dr to determine how long is the sequence in O(n)

    '''
    n = len(x)

    i = 1
    maxim = 0
    st = 0
    dr = 0
    while i < n:
      if int(getReal(x[i])) > int(getReal(x[i - 1])):
         j = i + 1
         if j < n:
            while int(getReal(x[j])) > int(getReal(x[j - 1])) and j < n - 1:
               j += 1
            if j - i + 1 > maxim:
               maxim = j - i + 1
               st = i
               dr = j
            i = j
      i += 1

    listOfStDr = []
    listOfStDr.append(st)
    listOfStDr.append(dr)

    return listOfStDr
    '''
    while st < dr:
      print (x[st]["real"], x[st]["sign"], x[st]["imaginary"])
      st += 1
    '''

def splitString(complexNumber):
    '''
    Splits the string into 3 parts and put them into a dictionar(real, sign, imaginary)
    '''
    dictionar = {"real": None, "sign": None, "imaginary": None}


    parts = complexNumber.split()
    if len(parts) == 3:
           setReal(dictionar, parts[0])
           if parts[1] == '-' or parts[1] == '+':
                   setSign(dictionar, parts[1])
           else:
                   print ("invalid format. Try 'a + bi' or 'a - bi'")
                   return None
           setImaginary(dictionar, parts[2])
           return dictionar
    else:
            print ("invalid format. Try 'a + bi' or 'a - bi")

def addNumber(complexList, dictNumber):
   val = splitString(dictNumber)
   if val != None:
      complexList.append(val)

def firstTenNumbers(list):
   addNumber(list, "1 + 5i")
   addNumber(list, "3 + 6i")
   addNumber(list, "4 - 5i")
   addNumber(list, "7 + 5i")
   addNumber(list, "8 + 6i")
   addNumber(list, "10 + 2i")
   addNumber(list, "3 + 8i")
   addNumber(list, "1 - 2i")
   addNumber(list, "2 - 7i")
   addNumber(list, "3 + 8i")

def main_ui():
    print("			 User interface")
    print("1. Add a complex number into the list.")
    print("2. Print all the numbers.")
    print("3. Choose a propery")
    print("4. Exit!")
    '''
    ListOfComeplexNumber - will store as a list of dictionaries all the values form (a + bi) "real", "sign", "imaginary"
    '''
    listOfComplexNumber = []
    firstTenNumbers(listOfComplexNumber)
    while True:
        value = input("-> ")
        if value == '1':
            complexNumber = input("Introduceti numarul: ")
            addNumber(listOfComplexNumber, complexNumber)
        if value == '2':
            printList(listOfComplexNumber)
        if value == '3':
            print ('1. Numbers that have their module between [0, 10]')
            print ('2. Longest seq that have their real part increasing ')
            value2 = input("-> insert a number: ")
            if value2 == '1':
                listOfStDr = longestSeqModule(listOfComplexNumber)
                printPartOfList(listOfComplexNumber, listOfStDr[0], listOfStDr[1])
            if value2 == '2':
                listOfStDr = longestSeqReal(listOfComplexNumber)
                printPartOfList(listOfComplexNumber, listOfStDr[0], listOfStDr[1])
        if value == '4':
            return

def run():
   while True:
      value = input("Press y/n to start-> ")
      if (value == 'y'):
         main_ui()
      elif value == 'n':
         return
      else:
         print ("Invalid command! Please try again.")

testsCreation()
run()
