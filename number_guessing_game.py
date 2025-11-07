# number guessing game

import random
num=random.randint(1,100)
n=int(input("enter the number between 1 and 100 "))
while n!=num:

    if n>num:
        print("your number is high guess lower ")
        
    elif n<num:
        print("your number is low guess higher ")
    n = int(input("Try again: "))
    
    

print("Number is correct! You guessed it.")
   
