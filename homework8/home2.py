filehandler = open("taxiprices.txt")
distance = float(input("Enter distance in kilometers: "))
cheapestPrice = 10000000000000
cheapestName = None
for taxi in filehandler:
    taxi = taxi.split(",")
    current = float(taxi[1]) + float(taxi[2]) * distance
    if current < cheapestPrice:
        cheapestPrice = current
        cheapestName = taxi[0]
        
print(cheapestName,"is the cheapest.")
filehandler.close()