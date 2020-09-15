finishCounter = 0
balance = int(input("Enter initial balance: "))
while finishCounter < 3:
    change = int(input("How did balance change? "))
    balance += change
    print ("The balance is",balance,"euros.")
    if balance > 0:
        finishCounter += 1
    else:
        finishCounter = 0
    if finishCounter == 3:
        print("Financial manager’s job is finished, terminating.")