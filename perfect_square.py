import math as mt
input_number=int(input("Enter a number to check if it is a Perfect Square:"))
root_number=int(mt.sqrt(input_number))
if root_number**2==input_number:
    print(input_number, 'is a Perfect Square')
else:
    print(input_number, 'is not a Perfect Square')