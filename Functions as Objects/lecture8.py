##**If the function does not have a return statement python explicitly returns none

def is_even(i):#function defintion
    i%2==0

print(is_even(5))#function call

#Function behaviour when we use print() statement within function

def add(x,y):
    return x+y
def mul(x,y):
    print(x*y)

add(1,2)
print(add(1,2))#evaluates to 3
mul(3,4)#prints 12
print(mul(4,5))#prints 20 and None

##print() is also a function

print(print(5))##evaluates to 5 and then None

##Example
def is_triangular(n):
    """ n is an int > 0 
Returns True if n is triangular, i.e. equals a continued
summation of natural numbers (1+2+3+...+k), False otherwise """
    total=0
    for i in range(n+1):
        total+=i
        if total==n:
            return(True)
    return (False)

print(is_triangular(10))
print(is_triangular(4))

##creating function for finding square root using bisection search

def sqr_root(n):
    low=0
    high=n
    epsilon=0.01
    guess=(low+high)/2
    while abs(guess**2-n)>=epsilon:
        if guess**2<n:
            low=guess
        else:
            high=guess
        guess=(low+high)/2
    return guess

print(sqr_root(4))
print(sqr_root(123))

##There are two types of environments:
##   *global environment(main program)
##   *function environment(function block)
##   *The variables used in function environment are formal parameters
##   *The variables used in global environment are input parameters which is later fed to(mapped to)
##    the formal parameters in the function block
##eg:

def f(x):##f is the function name,(x)= x is the formal parameter
    x=x+1
    return x
x=3##input variable
z=f(x)##function call (variable mapping to the function variable)
print(z)

##basically function is an object which is stored in memory that contains certain bunch of code
##we can use the same function with different name by assigning the function name with assignment operator(=)

##eg:
def is_even(i):
    return i%2==0
func=is_even
print(is_even(3))
print(func(4))

##function accessing another function(function as parameters):

def calc(op,x,y):
    return op(x,y)
def add(a,b):
    return a+b
def div(a,b):
    if b!=0:
        return a/b
    print("Denominator was 0.")
res=calc(add,2,3)
print(res)




    


        





        



