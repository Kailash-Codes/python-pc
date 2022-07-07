from re import X
from tkinter import Y


x = int(input("Enter value for x:"))
y = int(input("Enter value for y:"))
z = int(input("Enter value for z:"))

if x>y and x>z:
    print("x is Greatest")

elif y>z and y>x:
        print("Y is Greatest")

elif z>x and z>y:
            print("z is grestest")
