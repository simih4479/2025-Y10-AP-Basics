# Ask the user for their width and height
# (assume they put in valid data)
width = float(input("Width: "))
height = float(input("Height: "))
# calculate the area/perimeter
area = width * height
perimeter = 2 * (width+height)
# Output the area/perimeter
print()
print(f"perimeter: {perimeter} units")
print(f"Area: {area} square units")