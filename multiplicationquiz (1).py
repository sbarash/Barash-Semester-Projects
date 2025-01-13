#Sadie Barash
#1/09
#Multiplication Quiz

#Init
import random
import time
#Functions

def quiz():
    print("Welcome to the multiplication quiz!")
    score=0
    #Allows users to choose number of questions
    questions=int(input("How many questions would you like?"))
    #Allows users to choose difficulty level
    difficulty=(input("Select a mode: easy/medium/hard"))
    for i in range (questions):
        #Creates numbers based on difficulty level
        if difficulty=="easy":
            num1=random.randint(0,10)
            num2=random.randint(0,10)
        if difficulty=="medium":
            num1=random.randint(0,20)
            num2=random.randint(0,20)
        if difficulty=="hard":
            num1=random.randint(0,30)
            num2=random.randint(0,30)
        #Stores answer
        answer=(num1)*(num2)
        #Starts timer for user
        start_time=time.time()
        #Presents problem to user and asks for answer
        print("What is " + str(num1) + " multiplied by " + str(num2))
        user=int((input("input answer here")))
        #Prints correct/incorrect
        if answer==user:
            print("Correct!")
            score=score+1
        if answer!=user:
            print("Incorrect")
    end_time = time.time()
    #Determines amount of time passed
    elapsed_time=end_time-start_time
    #Gives user final result
    print("Time: " + str(elapsed_time) + " seconds")
    print("You got " + str(score) + " out of " + str(questions) + " questions correct")
#Main
quiz()
