def number_of_days(n):
    if n in {1,3,5,7,8,10,12}:
        return 31
    elif n in {4,6,9,11}:
        return 30
    elif n == 2:
        return 28
    else:
        return -1

while True:
    try:
        userInput = int(input("Enter number of month or 'done': "))
        if str(userInput) == "done":
            break    
        elif int(userInput) < 1 or int(userInput) > 12:
            print ("Number of month must be in the range 1-12")
        else:     
            print ("This month has",number_of_days(userInput),"days")
    except:
        print ("Please enter a valid number")
