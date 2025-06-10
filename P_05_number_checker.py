# Ask user for width until
# they enter a number that is more tham zero
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



# main routine goes here
for item in range (0, 2):
    width = num_check("Width: ")
    print(width)