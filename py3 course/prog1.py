from random import choice
def play(a,b):
    if a == "rock" and b == "paper":
        return "second"
    if a == b:
        return "draw"
    if a == "paper" and b == "rock":
        return "first"
    if a == "rock" and b == "scissors":
        return "first"
    if a == "scissors" and b == "rock":
        return "second"
    if a == "paper" and b == "scissors":
        return "second"
    if a == "scissors" and b == "paper":
        return "first"
computerCounter = 0
userCounter = 0
options = ["paper", "rock", "scissors"]
user1 = input("Enter your choice: ")
computer1 = choice(options)
fight1 = play(user1, computer1)
if fight1 == "first":
    userCounter += 1
    print ("Computer chose",computer1+". You won! You",userCounter,", computer",computerCounter,".")
if fight1 == "second":
    computerCounter += 1
    print ("Computer chose",computer1+". You lost! You",userCounter,", computer",computerCounter,".")
if fight1 == "draw":
    print ("Computer chose",computer1+". Draw. You",userCounter,", computer",computerCounter,".")
    
user2 = input("Enter your choice: ")
computer2 = choice(options)
fight2 = play(user2, computer2)
if fight2 == "first":
    userCounter += 1
    print ("Computer chose",computer2+". You won! You",userCounter,", computer",computerCounter,".")
if fight2 == "second":
    computerCounter += 1
    print ("Computer chose",computer2+". You lost! You",userCounter,", computer",computerCounter,".")
if fight2 == "draw":
    print ("Computer chose",computer2+". Draw. You",userCounter,", computer",computerCounter,".")
    
user3 = input("Enter your choice: ")
computer3 = choice(options)
fight3 = play(user3, computer3)
if fight3 == "first":
    userCounter += 1
    print ("Computer chose",computer3+". You won! You",userCounter,", computer",computerCounter,".")
if fight3 == "second":
    computerCounter += 1
    print ("Computer chose",computer3+". You lost! You",userCounter,", computer",computerCounter,".")
if fight3 == "draw":
    print ("Computer chose",computer3+". Draw. You",userCounter,", computer",computerCounter,".")
    
if userCounter == computerCounter:
    print("The game ended in a draw.")
elif userCounter > computerCounter:
    print("The game ended with your victory.")
else:
    print("The game ended with computer victory.")