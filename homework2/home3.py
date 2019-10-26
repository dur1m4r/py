def isInt(n):
    return int(n) == float(n)
distanceWhole = input("Enter length of power line (in meters): ")
distanceBetween = input("Enter maximumu distance between adjucment: ")
numberOfPoles = float(distanceWhole)/float(distanceBetween)

if isInt(numberOfPoles):
    numberOfPoles += 1
    print ("For this power line you need at least "+str(numberOfPoles)+" poles")
else:
    numberOfPoles += 2
    numberOfPoles = round(numberOfPoles)
    print ("For this power line you need at least "+str(numberOfPoles)+" poles")