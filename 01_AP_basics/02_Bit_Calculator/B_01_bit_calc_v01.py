# Generate Headings (eg: -----Heading-----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("instructions", "-")

    print('''
Instructions goes here.
-Instruction 1 
-Instruction 2
-etc
    ''')

# Ask users for their file type (integer/text/image/xxx)
def get_filetype():

    while True:
        response = input("File Type: ").lower()

        # Check for "i" or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if its an integer
        elif response in ['integer', 'int']:
            return 'integer'

        # check for an image
        elif response in ['image', 'picture', 'img', "p"]:
            return 'image'

        # check for text
        elif response in ['text', 'txt', 't']:
            return 'text'

        # if response is invalid output an error
        else:
            print("Please enter a valid file type")
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

def integer_calc():
    # ask the user to enter an integer (more than / equal to 0)
    integer = int_check("Integer: ", 0)
    # convert the integer to binary and work out the number of bits needed.
    raw_binary = bin(integer)
    # remove the leading 0b from the raw binary conversion
    binary = raw_binary [2:]
    num_bits = len(binary)
    #set up answer and return it
    answer = f"{integer} in binary is {binary}.  We need {num_bits} to represent it "

    return answer

def calc_text_bits():

    # Get text from user
    response = input("Enter some text....")

    # Calculate bits needed


    num_chars = len(response)
    num_bits = num_chars * 8
    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
       f"\nWe need {num_chars} x 8 bits to represent it"
       f"\nwhich is {num_bits} bits.")

    return answer

# Main routine goes here

#display instructions if requested
want_instructions= input("Press <enter> to read the instructions "
                         "or any key to continue.")
if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
         break

    # if user chose "i", ask if they want an image/integer
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)
