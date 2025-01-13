
#Madlibs

#Init


#Functions
def madlib():
    #Asks user to input info for Madlib
    print("Welcome to Sadie's Madlib Game!")
    print("Enter words to create a wacky story")
    adjective=input("Enter an adjective")
    noun=input("Enter a noun")
    place=input("Enter a place")
    pronoun=input("Enter possesive pronoun (his/her/their)")
    thing=input("Enter a thing")
    #Combines string to create Madlib story
    print("The " + adjective+ " " + noun + " " + "went to " + place + " to find " + pronoun + " " + thing)

#Main
madlib()
