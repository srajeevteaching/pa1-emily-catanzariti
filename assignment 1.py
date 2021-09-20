# Emily Catanzariti
# CS151, Dr. Rajeev
# 9/20/21
# Programming Assignment 1
# Program Inputs: length, width, and height of a room
# Program Outputs: the area of the room, the area of the room that needs to be painted, amount of primer needed to paint

# ask for the 3 definitions
length = input("What is the length of the room?")
width = input("What is the width of the room?")
height = input("What is the height of the room?")

# calculate the area
# ceiling
print("The area of the ceiling is")
print(length * width)
print("feet squared")
ceiling = (length * width)
# two walls
print("The area of the first two identical walls is")
print((height * length) * 2)
print("feet squared")
first_walls = ((height * length) * 2)
print("The area of the second two identical walls is")
print((height * width) * 2)
print("feet squared")
second_walls = ((height * width) * 2)

# total area that needs to be painted
total_area_painted = ceiling + first_walls + second_walls
print("The total area of the walls that needs to be painted is")
print(total_area_painted)
print("feet squared")

# gallons of primer
primer = total_area_painted / 200
print("The amount of primer needed in gallons for the total area is")
print(primer)
print("gallons")

# gallons of paint
paint = total_area_painted / 350
print("The amount of paint needed in gallons for the total area is")
print(paint)
print("gallons")
