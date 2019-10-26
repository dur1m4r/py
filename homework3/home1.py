userMonth = int(input("Enter month number: "))

months = {1: "January", 2: "February", 3:"March", 4: "April", 5: "May",
           6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
           11:"November", 12:"December"}

if userMonth <=0:
    print ("Month number must be in the range [1-12]")
else:
    outputMonth = months.get(userMonth, "The year has only 12 months")
    print (outputMonth)
      
