#Objects are the data which has a type
#the type of objects defines what kind of operations can be done to them

type(45)#int type
type(45.0)#float type
type(True)#bool type
type(False)#bool type
type(None)#Nonetype

#type conversions(casting)

float(19)
int(456.123)#takes only the integer part
int(0.8)#evaluates to zero
round(456)
int(round(44.6))

#combination of operatos and objects is expression

print(3+2)
print(3/2)
print(3-2)
print(3//2)
print(3**2)
print(3%2)
print(round((4/5)+2*3))

#variables are bound to a single object
#makes easier by simply invoking variable name to acess the objects
#expressions can also be bound to variables

a=12345
print(a)
print(a-45)

#program for finding volume of cube

side=4
volume=(side*side*side)
print(volume)

#other way

volume=(side**3)
print (volume)

#variable bindings can be changed

a=2#this binding had lost but exists somewhere in memory
b=6
a=b
print(a,b)

#swap values by using third variable

x=5
y=10
temp=x
print(temp)
x=y
print(x)
y=temp
print(y)

#python executes the instructions line by line


