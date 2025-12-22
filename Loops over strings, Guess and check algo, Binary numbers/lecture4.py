#Break statement used to terminate the loop
#Break statement ends the loop before it natural end comes
#Indentation should be given correctly to terminate the desired loop
#Eg:
mysum=0
for i in range(5,10):
    if i==5:
        print(i)
        break
        mysum+=1#the code block below break never gets executed
print(mysum)

#program for finding the number of even numbers in the range()
count=0
for i in range(5):
    if i%2==0:
        count+=1
print(count)

#program to check for letter i or u in a string
#using for loop
#loops over string
###type1(lengthy code)

s="my name is sundhar"
for i in range(len(s)):
    if s[i]=='i' or s[i]=='u':
        print("There is an i or u")
###type2(better one)
        
for char in s:  ##for loops can iterate directly through the characters in a string
    if char=='i' or char=='u':
        print("There is an i or u")

###type3(most efficient one)
for char in s:
    if char in "iu":
        print("There is an i or u")
###All the three programs above does the same thing but the code style is differnt

#pragram for finding unique characters in a string
a="hellosubash"
seen=""
count=0
for char in a:
    if char not in seen:
        seen+=char
        count+=1
print("count=",count)
print("seen=",seen)

#Guess and check alogorithm:
#start with a initial guess,if it provides solution,stop.
#otherwise,make a new guess to find solution.
#somepoint,guessing should have to be stopped for certain conditions

#Guess and check algo: finding Square root

guess=0
neg_flag=False
found=False#using flag as found(just a variable)
n=int(input("Enter a number to find sqr root:"))
if n<0:
    neg_flag=True
for i in range(abs(n)+1):
    guess+=1
    if guess**2==n:
        found=True
        print(f'square root of {n} is {guess}')
if not found:
    print(n,"is not a perfect square number")
if neg_flag:
    print("Just checking....did you mean",-n,"?")

#Guess and check can’t test an infinite number of values,you have to stop at some point

#Practice:
#--Hardcode a number as a secret number.
#--Write a program that checks through all the numbers from 1 to
#  10 and prints the secret value if it’s in that range. If it’s not
#  found, it doesn’t print anything.
#--How does the program look if I change the requirement to be:
#  If it’s not found, prints that it didn’t find it.

found=False
secret=8
for i in range(1,11):
    if i==secret:
        found=True
        print("found")
if not found:
    print("not found")

#Guess and check algo: finding cube root

cube=int(input("Enter the number to find cube root:"))
for guess in range(abs(cube)+1):
    if guess**3>=abs(cube):
        break
if guess**3==abs(cube):
    if cube<0:
        guess=-guess
    print(f'the cube root of {cube} is {guess}')
else:
    print(f'{cube} is not a perfect cube number')

#--Remember those word problems from your childhood?
#--For example:
#     -Alyssa, Ben, and Cindy are selling tickets to a fundraiser
#     -Ben sells 2 fewer than Alyssa
#     -Cindy sells twice as many as Alyssa
#     -10 total tickets were sold by the three people
#     -How many did Alyssa sell?
#     -Could solve this algebraically, but we can also use guess-and
#      check
found=False
for alyssa in range(11):
    if found:
        break
    for ben in range(11):
        if found:
            break
        for cindy in range(11):
            ben = alyssa-2
            cindy = 2*alyssa
            if alyssa+ben+cindy==10:
                found=True
                print(f"Alyssa sells {alyssa} tickets")
                print(f"Ben sells {ben} tickets")
                print(f"Cindy sells {cindy} tickets")
                break
#alternate method(efficient&simple)

for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            total=(alyssa+ben+cindy==10)
            b=ben==alyssa-2
            c=cindy==alyssa*2
            if total and b and c:
                print(f"Alyssa sells {alyssa} tickets")
                print(f"Ben sells {ben} tickets")
                print(f"Cindy sells {cindy} tickets")

#  --when the total tickets are higher , then the number of iterations will be higher.
#  --so, the program becomes slower because of nested loops.
#  --so, we can use single for loop and check the 2 codition , if true output the soultion.
#  --Take total tickets as 1000, ben=alyssa-20 , cindy=2*alyssa

#  most simple and efficient one
for alyssa in range(1001):
    ben=max(alyssa-20,0)
    cindy=2*alyssa
    if alyssa+ben+cindy==1000:
        print(f"Alyssa sells {alyssa} tickets")
        print(f"Ben sells {ben} tickets")
        print(f"Cindy sells {cindy} tickets")

#Program for decimal to binary conversion
flag=False
n=int(input("Enter an number:"))
result=""
if n==0:
    print("result=0")
while n>0:
    result=str(n%2)+result
    n=n//2
    flag=True
if flag:
    print("result=",result)



        


                






    



        
        
    
