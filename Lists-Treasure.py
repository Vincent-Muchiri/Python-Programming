from tkinter.tix import COLUMN
from turtle import position


row1 = ["0","0","0"]
row2 = ["0","0","0"]
row3 = ["0","0","0"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to hide your treasure? ")
column = int(position[0])
row = int(position[1])

print(f"your treasure will be hidden in row {row} column {column}")

column_index = column - 1
row_index = row - 1
row = map[row_index][column_index] = "X"

print(f"{row1}\n{row2}\n{row3}")