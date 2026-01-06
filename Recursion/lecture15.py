##Intro to Recursion:

##Multiplication for two values(using * operator):

def mult(a,b):
    return a*b

print(mult(5,4))

##Same operation in terms of iteration:
##Using For loop:
def mult1(a,b):
    mul=0
    for i in range(b):
        mul+=a
    return mul

print(mult1(5,4))

##Using while loop:

def mult2(a,b):
    mul=0
    while b>0:
        mul+=a
        b-=1
    return mul

print(mult2(100,25))

##Recursion:
##    *Analyzing the pattern present in a given problem and repeating the same function
##    until the base case .
##    *Recursive case calls the same function (itself) to provide the solution for a problem.
##    *Base case provides the stop of the program.
##    *The chained function calls , waits for return value which is given by the succeeding function call.
##    *A same function calls itself for a specific number of times is called recursion.
##    *In recursion each function call is separate , also their environment also separate , which means independent to each  other(except return value).

##Multiplication for two values(using recursion):

def mul_recursion(a,b):
    if b==1:##base case
        return a
    else:
        return a+mul_recursion(a,b-1)##recursive case

print(mul_recursion(10,4))

##Example
## Complete the function that calculates n**p for variables n and p
def power_recur(n, p):
    if p==1:
        return n
    elif p==0:
        return 1
    else:
        return n*power_recur(n,p-1)

print(power_recur(2,3))

##Factorial calculation using recursion:

def factorial_recur(a):
    if a==0 or a==1:
        return 1
    else:
        return a*(factorial_recur(a-1))

print(factorial_recur(5))
        


    

