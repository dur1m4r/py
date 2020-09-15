from random import sample
def bingo():
    bingoList = []
    firstThree = sample(range(1,11),3)
    for i in firstThree:
        bingoList.append(i)

    secondTwo = sample(range(11,21),2)
    for i in secondTwo:
        bingoList.append(i)

    one = bingoList.count(1)
    two = bingoList.count(2)
    three = bingoList.count(3)
    if one + two + three == 3:
        bingo()
    return bingoList

print(bingo())