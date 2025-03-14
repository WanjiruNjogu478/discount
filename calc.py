num1 = float(input("Enter the first no."))
num2 = float(input("Enter the second no."))
operation = input("Enter (*,/,-,/):")

#perform the operation and give the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Cnnot divide by 0")

else:
    print("Invalid operation!Please choose (-,/,* or+)")