from turtle import *
from easygui import *
def horizontal(n):
    for i in range(n):
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
    left(180)
    forward(50 * int(n))
    left(90)
def cell(n, m):
    horizontal(n)
    for i in range(m-1):
        forward(50)
        left(90)
        horizontal(n)
    
     
title("Grid")
rows = integerbox("How many rows grid should have? ")
columns = integerbox("How many columns grid should have?")

cell(rows, columns)


exitonclick()