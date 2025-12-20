###While loop:
#1)while loop for iterating a code block

n=1#loop variable
while n<=5:#tests condition with loop var
    print("$"*n)#code block
    n+=1#incrementation

n=5#loop variable
while n>0:#tests condition with loop var
    print("$"*n)#code block
    n-=1#decrementation

#2) Expand this code to show a sad face when the user entered the
#while loop more than 2 times.
# Hint: use a variable as a counter
#where = input("Go left or right? ")
#while where == "right":
#where = input("Go left or right? ")
#print("You got out!")
n=0
where = input("Go left or right? ")
while where == "right":
    where = input("Go left or right? ")
    n+=1
    if n>=2:
        print(":(")
        
print("You got out!")

#3)factorial calculation using while loop

fact=1
i=1
n=int(input("Enter a number to find its factorial:"))
while i<=n:
    fact*=i
    i+=1
print(f'{n} factorial is {fact}')

###For loop
#inc/dec and the loop variable are defined inside the syntax of the for loop

for i in range(1,4,1):#range(start,stop,step)
    print(i)

for i in range(5,0,-1):
    print("*"*i)

#1)running sum in for loop

mysum=0
for i in range(10+1):
    mysum+=i
print(mysum)

#2)factorial using for loop

n=int(input("Enter a number to find its factorial:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(f'{n} factorial is {fact}')
