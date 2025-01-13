#Guessing Game

#init
import random

#functions

def game():
    #Creates initial score for user
    points=30
    print("Welcome to the random number guessing game! You will have three chances to guess the correct number!")
    print("You start with 30 points. You lose 10 points every round you guess incorrectly.")
    level = int(input("What level would you like to play (1, 2, or 3)?")) #Allows user to pick level and customizes number range based on that
    if level==1:
        secret = random.randint(0,10)
    if level==2:
        secret = random.randint(0,20)
    if level==3:
        secret = random.randint(0,30)
    guess_one = int(input("Enter Guess One")) #Stores users first guess
    #Evaluates secret number against guess and updates score accordingly
    if secret==guess_one:
        print("Congrats! You guessed the correct number!")
    if guess_one>secret:
        print("Sorry! Your guess was too high. Try again!")
        points=points-10
    if guess_one<secret:
        print("Sorry! Your guess was too low. Try again!")
        points=points-10
    if guess_one>secret or guess_one<secret:
        guess_two = int(input("Enter Guess Two"))
        if secret==guess_two:
            print("Congrats! You guessed the correct number!")
        if guess_two>secret:
            print("Sorry! Your guess was too high. Try again!")
            points=points-10
        if guess_two<secret:
            print("Sorry! Your guess was too low. Try again!")
            points=points-10
        if guess_two>secret or guess_two<secret:
            guess_three = int(input("Enter Guess Three"))
            if secret==guess_three:
                print("Congrats! You guessed the correct number!")
            else:
                print("Sorry! You did not guess the correct number after three tries and lost the game.")
                points=points-10
            #Tells user the secret number and their point total
            print("The secret number was" + " " + str(secret))
            print("You got" + " " + str(points) + " " + "points")
   #Allows user to play again or ends game
    play_again = input("Want to play again (y/n)?")
    if play_again == "y":
        game()
    else:
        print("Thanks for playing!")


#main
game()
