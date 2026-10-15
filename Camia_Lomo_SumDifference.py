# GLOBAL VARIABLES
addition = []
subtraction = []
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

def calculate_sum():
    global number1, number2, addition
    # LOCAL VARIABLE - ADDITION
    addition = number1 + number2
    print("Sum: ", addition)

def calculate_difference():
    global number1, number2, subtraction
    # LOCAL VARIABLE - SUBTRACTION
    subtraction = number1 - number2
    print("Difference: ", subtraction)

calculate_sum()
calculate_difference()
