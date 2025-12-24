
#Finding binary for a decimal fraction
x=float(input("Enter a number between 0 and 1:"))
p=0
while(x*(2**p)%1 != 0):
    print("the remainder=",str((x*(2**p)- int(x*(2**p)))))
    p+=1
num=int(x*(2**p))
result=''
if num==0:
    print("result=",0)
while num>0:
    result=str(num%2)+result
    num=num//2
for i in range(p-len(result)):
    result="0"+result

result=result[0:-p]+'.'+result[-p:]
print(f'The binary representation of the decimal {x} is {result}')

##Approximation algorithm:
##    *In this alogorithm,we can't find the exact solution(in some case) but we can able to find the
##    approximation value which is close to the solution.
##    *In guess and check algo,we make an guess if it provides the solution , we stop , otherwise
##    we keep making guessing upto certain limit.
##    *Two parameters of approximation algorithm:
##        Epsilon => range or (+/-)boundary
##        Increment => how much the guesses to be incremented.
##    *integers are used as a guess in (guess and check).
##    *Floating numbers are used in approximation algorithm

##Finding square root of a number using approximation method(non perfect square numbers)

epsilon=0.01
guess=0
num_guesses=0
x=int(input("Enter an number:"))
increment=0.0001
while (((guess**2)-x)<=epsilon) and guess**2 <= x:
    guess+=increment
    num_guesses+=1
print("num_guesses=",num_guesses)
print(guess,'is close to square root of', x)



    



        



