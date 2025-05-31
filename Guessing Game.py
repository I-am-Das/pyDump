import time 
import random 

name1=input("ENnter player 1 Name :")
name2=input("ENter player 2 Name :")
print("Hello {} and {}".format(name1,name2))
print("The computer is going to generate some 5 numbers")
print("You have to select 3 numbers")
num=[]
while(len(num)!=5):
    d=random.randint(1,10)
    if (d in num):
        continue 
    else:
        num.append(d)

player1=[]
player2=[]
p1=0
p2=0

for i in range(3):
    print("Enter your guess {}".format(name1))
    a=int(input())
    while (a in player1 or a in player2):
        a=int(input("Enter another number :"))
    if(a not in player1 or a not in player2):
        player1.append(a)
        if (a in num):
            print("Correct Guess")
            p1+=1
        else:
            print("Wrong")
    print("Enter your guess {}".format(name2))
    a2=int(input())
    while (a in player1 or a in player2):
        a=int(input("Enter another number :"))
    if(a2 not in player1 or a2 not in player2):
        player2.append(a2)
        if (a2 in num):
            print("Correct Guess")
            p2+=1
        else:
            print("Wrong")

print("=======================================================")

print("{} guessed the numbers {}".format(name1,player1))
print("{} guessed the numbers {}".format(name2,player2))


print("=======================================================")
if (p1>p2):
    print("{} is the WINNER and SCORED {}".format(name1,p1))
else:
    print("{} is the WINNER snd SCORED {}".format(name2,p2))
print("=======================================================")

    