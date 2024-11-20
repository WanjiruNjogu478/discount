# a block of code that perform specific operation (s)

# def add(): 1 usage
#     print(x+y)

# y = 7
#
# if y % 2 > 0:
#     print("odd")
# else:
#     print("even")


# Function to check if a number is odd or even
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is odd or even and print the result
result = check_odd_even(number)
print(f"The number {number} is {result}.")

