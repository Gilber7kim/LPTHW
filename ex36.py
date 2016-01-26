from random import randint
import time
import os,sys
import sys,string
import string


def selfIntroduce():
    print "Hello, this is Gilbert."
    name = raw_input("What is your name? ")
    print "So your name is "+name+". Welcome "+name+"!"

    if "David" in name:
        stupid_david()
    else:
        permission()

def permission():
    print "Do you want to play a game with me? [y/n]"
    choice = raw_input("> ")

    if choice == "y":
        dice()
    elif choice == "n":
        print("bye!")
        exit(0)
    else:
        print("Why can't you type y or n? I don't want to play with dumb. Bye!")
        exit(0)


def stupid_david():
    print "Oh, actually all the Davids cannot play this game. Blame David lee :)"
    exit(0)


def dice():
    import random
    print("Win me with the dice.")
    print("You should have a higher number than three.")
    raw_input("Enter to continue")
    number = random.randint (1, 6)
    if number == 1:
        print ("[----------------]")
        print ("[----------------]")
        print ("[-------()-------]")
        print ("[----------------]")
        print ("[----------------]")
        print("Jump out.")
        exit(0)
    if number == 2:
        print ("[----------------]")
        print ("[----------------]")
        print ("[--()--------()--]")
        print ("[----------------]")
        print ("[----------------]")
        print("Loser.")
        exit(0)
    if number == 3:
        print ("[-()-------------]")
        print ("[----------------]")
        print ("[-------()-------]")
        print ("[----------------]")
        print ("[-------------()-]")
        print("That was close, dude.")
        exit(0)
    if number == 4:
        print ("[-()----------()-]")
        print ("[----------------]")
        print ("[----------------]")
        print ("[----------------]")
        print ("[-()----------()-]")
        print("You're pretty lucky.")
        next_step()
    if number == 5:
        print ("[-()----------()-]")
        print ("[----------------]")
        print ("[-------()-------]")
        print ("[----------------]")
        print ("[-()----------()-]")
        print("Congrats!")
        next_step()
    if number == 6:
        print ("[-()----------()-]")
        print ("[----------------]")
        print ("[-()----------()-]")
        print ("[----------------]")
        print ("[-()----------()-]")
        print("Congrats!")
        next_step()


def next_step():
    print("Here's the next game.")
    print("You have to get the right answer for this multiple-choice question.")
    print("You stayed up all night playing video game. And now, you are in Pastor Johnson's class.")
    print("What should you do?")
    print("a. sleep")
    print("b. stand up to get rid of sleepiness")
    print("c. shout")
    print("d. ask for permission to go to the toilet")
    print("Gimme an alphabet you think it's the answer.")
    choice = raw_input("> ")

    if choice == "a":
        print("OH MAN! No one can sleep in my class!")
        print("Game Over")
        exit(0)
    elif choice == "b":
        print("This is not a Montesory-bang! Sit down!")
        print("Game Over")
        exit(0)
    elif choice == "c":
        print("Well done. You got rid of your exhaustion, and Paul was caught instead of you.")
        print("All Clear")
        exit(0)
    elif choice == "d":
        print("What did you do in the lunch time? No!")
        print("Game Over")
        exit(0)
    else:
        print("alphabet, Please.")
        exit(0)

selfIntroduce()
