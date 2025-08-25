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
def image_calc():
    # get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)
    # calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24


    #set up answer and return it
    answer = f"Number of pixels:  {width} x {height} = {num_pixels} " \
             f"\nNumber of bits: {num_pixels} x 24 = {num_bits}"

    return answer

# main routine goes here
image_ans = image_calc()
print(image_ans)