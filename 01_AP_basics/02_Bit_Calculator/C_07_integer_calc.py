# Ask user for width until
# they enter a number that is more tham zero
def int_check(question: object, low: object) -> object:

    error = f"Please enter a number that is more than {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# calculate how many bits needed to represent an integer
def integer_calc():
    # ask the user to enter an integer (more than / equal to 0)
    integer = int_check("Integer", 0)

    # convert the integer to binary and work out the number of bits needed.
    raw_binary = bin(integer)
    # remove the leading 0b from the raw binary conversion
    binary = raw_binary [2:]
    num_bits = len(binary)

    #set up answer and return it
    answer = f"{integer} in binary is {binary}.  We need {num_bits} to represent it "

    return answer

# main routine goes here
image_ans = integer_calc()
print(integer_ans)