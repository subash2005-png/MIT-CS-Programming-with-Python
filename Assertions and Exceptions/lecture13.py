##Exceptions:
##    *Exceptions are the errors arises when the unexpected condition gets evaluated.
##    *Try and except statements can be used to handle these exceptions.
##    *Try block gets evaluated until the unexpected condition arises or invalid input is fed.
##    *In such cases,except block will be evaluated.
##    *Instead of showing error(option) , the statements inside except block is excepted.
##example

def sum_num(s):
    total=0
    for char in s:
        if char in "0123456789":
            c=int(char)
            total+=c
    return total

print(sum_num("1234"))
print(sum_num("1234abcde"))

##to handle exceptions 
def sum1_num(s):
    """ s is a non-empty string containing digits.
        Returns sum of all chars that 
        are digits """
    total=0
    for char in s:
        try:
            c=int(char)
            total+=c
        except:
            print("Can't convert character:",char)
    return total
print(sum1_num("1234"))
print(sum1_num("1234abcde"))

##User input can lead to exceptions

def div():
    try:
        a=int(input("Enter a number 1:"))
        b=int(input("Enter a number 2:"))
        print(a/b)

    except:
        print("bug in input")
div()

##can have separate except blocls to handle with a particular type of exception.

##When there is an exception , we can raise our own error statement using raise

##Example

def sum2_num(s):
    total=0
    for char in s:
        try:
            c=int(char)
            total+=c
        except:
            raise TypeError("string cannot be computed with int")
    return total

print(sum2_num("1234"))
#print(sum2_num("1234abcde"))##type error

##example
def pairwise_div(Lnum, Lden):
    """ Lnum and Lden are non-empty lists of equal lengths containing numbers
        Returns a new list whose elements are the pairwise 
        division of an element in Lnum by an element in Lden. 
        Raise a ValueError if Lden contains 0"""
    l=[]
    for i in range(len(Lnum)):
        try:
            c=Lnum[i]/Lden[i]
            l.append(c)
        except:
            raise ValueError("Division by zero not possible")
    return(l)

l1=[10,8,6]
l2=[5,4,3]
print(pairwise_div(l1,l2))


##Assert statement:
##    *assert statement used to stop(halt) the execution of the program if there is any exceptions
##    in input.
##    *It arises an asserion error depending upon the exception statement inside it.
##    *It can be used anywhere which helps to locate the bug.

##example
def sums_num(s):
    """ s is a non-empty string containing digits.
        Returns sum of all chars that 
        are digits """
    assert len(s)!=0 , "string is empty"
    total=0
    for char in s:
        try:
            c=int(char)
            total+=c
        except:
            print("Can't convert character:",char)
    return total

string=""
print(sums_num(string))






        
