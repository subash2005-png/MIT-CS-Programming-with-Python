##Functions:
##    *A fuction is a self contained block which contains one or more statement the does specific
##    task when the function is called.
##    *syntax for function:-
##        def<function name>(parameters):
##    where def is a keyword,and parameters are like inputs fed to the function blocks.
##    *Once we defined a function,we can use it multiple times by using function call.
##    *A function code only runs when we call the function.

## Examples for creating and calling a function

## To find whether a number is even

def is_even(a):#defining a function
    """
      a is a positive int
      returns true if a is even otherwise returns false
    """
    return a%2==0

print(is_even(16))##function call
print(is_even(9))

##To find the length of string

def lens(b):
    sum=0
    lens=0
    i=0
    while b[i]!=b[-1]:
        lens+=1
        i+=1
    return (lens+1)
print(len("subash"))
c="qwertyuioplkjhgfdsazxcvbnm"
print(len(c))

##
def div_by(n,d):
    """ n and d are ints > 0
Returns True if d divides n evenly and False otherwise """
    if n%d==0:
        return True
    else:
        return False
print(div_by(1,3))
print(div_by(150,15))

##To add all the odd integers between (and including) a and b
##Using for loop:
def sum_odd(a,b):
    sum=0
    for i in range(a,b+1):
        if i%2==1:
            sum+=i
    return sum

print(sum_odd(1,9))

##Using while loop:
def sum1_odd(a,b):
    sum=0
    while a<=b:
        if a%2==1:
            sum+=a
        a+=1
    return sum

print(sum1_odd(1,9))

##function for finding palindrome or not
def palindrome(s):
    if s[::-1]==s[:]:
        return True
    else:
        return False
k="malayalam"
d="abcdefg"
c="racecar"
print(palindrome(k))
print(palindrome(d))
print(palindrome(c))









