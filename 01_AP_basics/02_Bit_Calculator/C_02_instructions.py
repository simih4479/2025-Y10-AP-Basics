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


# Main routine goes here

#display instructions if requested
want_instructions= input("Press <enter> to read the instructions"
                         "or any key to continue.")
if want_instructions == "":
    instructions()


print("program continues")


