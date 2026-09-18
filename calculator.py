num1 = float(input("Enter first number : "))
operator = input("Enter Operator : ")
num2 = float(input("Enter Second number : "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        result = "Error : Cannot divide by zero!"
    else:
        result = num1 / num2

print("Result = ",result)