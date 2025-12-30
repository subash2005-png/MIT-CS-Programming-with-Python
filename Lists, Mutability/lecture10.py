##Lists:
##    *Generally , lists are indexable ordered sequence of objects.
##    *It is mutable,which means the element/object inside the  list can be changed.
##    *It doesn't create new object , it mutates itself depending upon function.

##eg:
l=[1,2,3,4,5,6]
l[2]=0
print(l)

##L.append(element) is used to add an element at the end of the list

l.append(7)
print(l)

l=l.append(7)
print(l)#returns none because the append() function completes it tasks of mutating the list
#        assigning it to other variable causes none to return

L1=["hello"]
L2=["everyone"]
L3=["hi"]
L4=L1+L2#concatenation of lists creates new object(i.e not mutating)
print(L4)
L3.append(L4)##it creates sub-lists indicate that only one element to be added at the end of the list
print(L3)
l=L1.append(L3)
print(l)

##    *Some functions mutate the list and don't return anything

##practice problems
##1)
def make_ordered_list(n):
    """ n is a positive int
Returns a list containing all ints in order 
from 0 to n (inclusive)
"""
    list=[]
    for i in range(n+1):
        list.append(i)
    return list

print(make_ordered_list(10))

##2)
def remove_elem(L, e):
    """L is a list ,Returns a new list with elements in the same order as L
       but without any elements equal to e. 
    """
    list=[]
    for i in L:
        if i != e:
            list.append(i)
    return list
L=[1,2,2,2,1,1,5,6]
print(remove_elem(L,2))

##string to list
##     -- syntax: list(s)
##     -- s.split(),split a string on a character parameter
##Examples:
s="anandhavalli@123"
L=list(s)##creates each and every character in a string as a individual element in a list
print(L)

L1=s.split(' ')
print(L1)
Li=s.split('d')
print(Li)

##3)
def count_words(sen):
    """ sen is a string representing a sentence 
Returns how many words are in s (i.e. a word is a 
a sequence of characters between spaces. """
    L=sen.split(' ')
    return len(L)

print(count_words("Hello it's me"))

##List operations:
##    *sort()
##    *reverse()
##    *sorted()
##    *sort() and reverse() are used to mutate the list , but sorted list
##    is assigned to new object instead of mutating the list itself.

##example
list1=[9,8,7,6,5,4,3,2,1]
list1.sort()
print(list1)
list1.reverse()
print(list1)
list2=sorted(list1)
print(list2)##returns sorted version of list1(no mutation)

##4)
def sort_words(sen):
    """ sen is a string representing a sentence 
        Returns a list containing all the words in sen but
        sorted in alphabetical order. """
    list=sen.split(' ')
    list.sort()
    return list
print(sort_words("look at this photograph"))

##List supports iteration:

def square_list(L):
    l=[]
    for elem in L:
        b=elem**2
        l.append(b)
    return l
L=[1,2,3,4,5]
print(square_list(L))

##tricky example 1
##Range() returns something that behaves like a tuple
lis1=[1,2,3,4]
for i in range(len(lis1)):##i=0,1,2,3
    lis1.append(i)
print(lis1)##lis1=[1,2,3,4,0,1,2,3]

##tricky example 2

##lis2=[1,2,3,4,5]
##i=0
##for e in lis2:
##    lis2.append(i)
##    i+=1 ##this program never gets stopped because for loop iterates through the mutating list
##    print(lis2)

##to combine more than one element in a list extend() is used.
li1=[2,4,5]
li1.extend([7,8,9])
print(li1)

##    To clear all the elements in a list and to make it as a empty list
##    clear() is used
##example

listt=[1,2,3,4,4,4,4,4]
listt.clear()
print("listt=",listt)





        



    

    

    

    
