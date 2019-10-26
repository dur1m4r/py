url = input("Please enter URL: ")
url = url.split("/")
counter = 0
for i in url:
    if i.startswith("~"):
        print ("Username is",i[1:])
        counter += 1
if counter == 0:
    print ("Username not found")