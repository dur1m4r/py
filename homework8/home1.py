filename = input("Enter filename: ")
try:
    counter = 1
    filehandler = open(filename)
    for line in filehandler:
        print(str(counter)+". "+line)
        counter += 1
except:
    print("Some error occuried, chech your data and run program again")
    
filehandler.close()    

    