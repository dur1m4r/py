def more_than_three(lst):
    outputLst = []
    counter = 0
    for i in range(len(lst)):
        if lst[i] > 3:
            outputLst.append(counter)
            counter += 1
        else:
            outputLst.append(counter)
    return outputLst


print(more_than_three([5, 2, 1, 8, 21, 7, 3, 4]))
print(more_than_three([4, 4, 4, 4, 4]))