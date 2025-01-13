#Rock, Paper, Scissors

#Init
import random
#Functions

def rock_paper_scissors():
    print("Welcome to Rock Paper Scissors")
    #Creates variables and sets all scores to zero
    player_score=0
    computer_score=0
    ties=0
    while True:
        print("Make your move!")
        #User move
        player_move_input=input("Rock, Paper, Scissors, Go:")
        player_move=player_move_input.capitalize()
        #Creates computer move
        computer_move=random.randint(1,3)
        #1=rock, 2=paper, 3=scissors
        #Evaluates user move against computer move
        if computer_move==1:
            computer_move = "Rock"
            print("The computer's move is rock")
        if computer_move==2:
            computer_move = "Paper"
            print("The computer's move is paper")
        if computer_move==3:
            computer_move = "Scissors"
            print("The computer's move is scissors")
        if player_move=="Rock" and computer_move=="Rock":
            print("It's a tie!")
            ties=ties+1
        if player_move=="Rock" and computer_move=="Paper":
            print("You lost. Please try again!")
            computer_score=computer_score+1
            computer_score==computer_score + 1
        if player_move=="Rock" and computer_move=="Scissors":
            print("You won!")
            player_score=player_score+1
        if player_move=="Paper" and computer_move=="Rock":
            print("You won!")
            player_score=player_score+1
        if player_move=="Paper" and computer_move=="Paper":
            print("It's a tie!")
            ties=ties+1
        if player_move=="Paper" and computer_move=="Scissors":
            print("You lost. Please try again!")
            computer_score=computer_score+1
        if player_move=="Scissors" and computer_move=="Rock":
            print("You lost. Please try again!")
            computer_score=computer_score+1
        if player_move=="Scissors" and computer_move=="Paper":
            print("You won!")
            player_score=player_score+1
        if player_move=="Scissors" and computer_move=="Scissors":
            print("It's a tie!")
            ties=ties+1
        #Displays score
        print("Player score: " + str(player_score))
        print("Computer score: " + str(computer_score))
        print("Ties: " + str(ties))
        play_again=str(input("Do you want to keep playing (y/n)"))
        #Restarts or ends game
        if play_again=="y":
            print("restarting...")
        if play_again=="n":
            print("Thanks for playing!")
            break

#Main
rock_paper_scissors()


