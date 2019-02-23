import math


# Setters and getters

def setSign(dictionar, sign):
	dictionar["sign"] = sign

def setReal(dictionar, real):
	dictionar["real"] = real

def setImaginary(dictionar, imaginary):
	dictionar["imaginary"] = imaginary

def printList(listOfComplexNumber):
   for comp in listOfComplexNumber:
      print (comp)

def getReal(dictionar):
   return dictionar["real"]

def getImaginary(dictionar):
   return dictionar["imaginary"]

# End of setters and getters

def creationNumber(number, sign):
    '''
    Transforms the digits of the string of imaginary part into an integer
    input - string
    return - integer
    '''
    nr = 0
    for x in number:
        if x >= '0' and x <= '9':
            nr = nr * 10 + int(x)
    if sign == '-':
        return -nr
    return nr

def moduleOfNumbers(complexNumber):
   '''
return the module of a complex number
input - dictionary
return - float
   '''
   nr1 = complexNumber[0]
   nr2 = complexNumber[1]

   return math.sqrt(nr1 * nr1 + nr2 * nr2)

def longestSeqReal(x):
   '''
   n = how many numbers we have
   We use st and dr to determine how long is the sequence in O(n)
   
   '''
   list = [0, 0]
   n = len(x)
   print("n este: " + str(n))
   i = 1
   maxim = 0
   st = 0
   dr = 0
   while i < n:
      if int(x[i][0]) > int(x[i - 1][0]):
         j = i + 1
         if j < n:
            while int(x[j][0]) > int(x[j - 1][0]) and j < n - 1:
               j += 1
            if j - i + 1 > maxim:
               maxim = j - i + 1
               st = i
               dr = j
            i = j
      i += 1

      list[0] = st
      list[1] = dr
      return list
    
    
def testPrint(x, st, dr):
     while (st < dr):
        print (x[st][0], x[st][1])
        st += 1
   
         
def splitString(complexNumber):
   '''
   Splits the string into 3 parts and put them into a dictionar(real, sign, imaginary)
   '''

   listOftuples = []
   parts = complexNumber.split()
   if len(parts) == 3:
           tuples = (int(parts[0]), creationNumber(parts[2], parts[1]))
           return tuples
   else:
           print ("invalid format. Try 'a + bi' or 'a - bi'")

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
            for x in listOfComplexNumber:
               module = moduleOfNumbers(x)
               if module >= 0 and module <= 10:
                  print (x[0], x[1])
         if value2 == '2':
            l = longestSeqReal(listOfComplexNumber)
            st = l[0]
            dr = l[1]
            while (st < dr):
                print (listOfComplexNumber[st][0], listOfComplexNumber[st][1])
                st += 1
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

run()
