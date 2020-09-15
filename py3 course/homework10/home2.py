from easygui import *
from datetime import *
def monthBday(n):
    if n == 1:
        return "January"
    if n == 2:
        return "February"
    if n == 3:
        return "March"
    if n == 4:
        return "April"
    if n == 5:
        return "May"
    if n == 6:
        return "June"
    if n == 7:
        return "July"
    if n == 8:
        return "August"
    if n == 9:
        return "September"
    if n == 10:
        return "October"
    if n == 11:
        return "November"
    if n == 12:
        return "December"
name = enterbox("What is your name?")
year = integerbox("What year you were born?", lowerbound = 1900, upperbound = 2015)
month = integerbox("What month you were born?")
month = monthBday(month)
day = integerbox("What day of a month you were born?")
age = datetime.now().year - year
msgbox("Hello, "+name +"\nYour birth date is "+month+" "+str(day)+", "+str(year)+"\nYou are "+str(age)+" years old")
