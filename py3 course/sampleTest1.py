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
    
print(play("scissors","scissors"))