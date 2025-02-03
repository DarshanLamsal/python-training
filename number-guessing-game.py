import random
number=random.randint(1,10)
guess=0

#asking the user to input the number until they guess it correctly
while guess!=number:

    #prompting the user to input numbers between 1-10
    guess=int(input("Enter a number between 1 and 10:"))

    #informing the user that the guessed number is lower than the actual number
    if guess<number:
        print("Your guess is lower than the number :(")

    #informing the user that the guessed number is higher than the actual number
    elif guess>number:
        print("Your guess is higher than the number :(")

    #asking the use to input numbers between 1-10 in case user doesn't input numbers between 1-10 
    elif guess < 1 or guess > 10:
       print("Error X(  Please enter a number between 1 and 10.")
   
   # congratulating the user if the user guesses correctly
    else:
        print("You guessed the number :)")