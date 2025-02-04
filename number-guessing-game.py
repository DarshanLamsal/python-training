import random
number=random.randint(1,10)
guess=0
attempts=0
#asking the user to input the number until they guess it correctly
while guess!=number :

    #setting the amount of guess that is required to finish the game as 3
    if attempts==3:
        print(f"You ran out of guesses :(  The secret number was {number}.")
        break
    #prompting the user to input numbers between 1-10
    guess=int(input("Enter a number between 1 and 10:"))

    #asking the use to input numbers between 1-10 in case user doesn't input numbers between 1-10 
    if guess < 1 or guess > 10:
       print(f"Error X(  Please enter a number between 1 and 10. You have {2-attempts} guesses left.")
   
    #informing the user that the guessed number is higher than the actual number
    elif guess>number:
        print(f"Your guess is higher than the number :(. You have {2-attempts} guesses left.")

    #informing the user that the guessed number is lower than the actual number
    elif guess<number:
        print(f"Your guess is lower than the number :(. You have {2-attempts} guesses left.")

   # congratulating the user if the user guesses correctly
    else:
        print("You guessed the number :)")

    #increasing the number of attempts that the user has inputted 
    attempts+=1