try:
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")
    filehandler = open(source)
    filehandler2 = open(destination, "w")
    counter = 0
    for line in filehandler:
        counter = counter + line.count("hello")
        line.replace("hello","hi")
        line.replace("Hello","Hi")
        filehandler2.write(line)
    filehandler.close()
    filehandler2.close()
    print(counter,"replacements were made.")
except:
    print("Error")

