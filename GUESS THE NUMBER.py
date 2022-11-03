import random
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
n = random.randint(lower,upper)
guess = int(input("Guess a Number : "))
count=0
while n != "guess":
    if guess < n:
        count=count+1
        print("guess is low")
        guess = int(input("Guess a Number "))
        
    elif guess > n:
        count=count+1
        print("guess is high")
        guess = int(input("Guess a Number "))
        
    else:
        count=count+1
        print("Congratulations you did it in " ,count, "try")
        break
