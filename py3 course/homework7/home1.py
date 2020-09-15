name = input("Enter first name: ")
name = name[0].upper() + name[1:].lower()
grades = input("Enter grades: ")
grades=grades.upper()
print("Hello",name+", your grades are",grades)
print("You have",len(grades),"grades")
print("Last grade is",grades[len(grades)-1])
counter = 0
for grade in grades:
    if grade =="A" or grade == "B":
        counter+= 1
        
print("The number of A`s and B`s is",counter)