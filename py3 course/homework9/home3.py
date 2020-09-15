def listTrip(file,budget):
    content = open(file)
    directions = []
    for line in content:
        line = line.split(";")
        if int(line[1]) <= budget:
            directions.append(line[0])
    content.close()
    return directions

budget = int(input("Enter trip budget: "))
print("Suitable trips are:")
counter = 0
for i in listTrip("trips.txt", budget):
    print (i)
    counter += 1
if counter == 0:
    print("There are none")
