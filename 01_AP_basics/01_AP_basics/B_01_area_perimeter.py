# Ask user for width until
# they enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            Response = float(input(question))

            # check that the number is more than zero
            if Response > 0:
                return Response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine starts here...

keep_going = ""
while keep_going == "":

     # Get width and height
     width = num_check("Width: ")
     height = num_check("Height: ")
     # calculate area/perimeter
     area = width * height
     perimeter = 2 * (width + height)
     # Display output
     print()
     print(f"perimeter: {perimeter} units")
     print(f"Area: {area} square units")

     # Ask user if they want to keep going
     keep_going = input("Press enter to keep going or any key to quit")
     print()
print("Thank you for using the area / perimeter calculator")
