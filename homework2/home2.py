name = input("Enter your name: ")
footSize = input("Enter your foot size (cm): ")
shoeSize = round(1.5 * (float(footSize) + 1.5))
print ("Dear "+name+", your shoe size is "+str(shoeSize))