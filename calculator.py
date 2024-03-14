first = input("Enter your first number")
first = int(first)
operator = input("Enter Operator (+,-,/,*,% )" )
second = input("Enter your Second Number")
second = int(second)
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    print(first / second)
elif operator == "*":
    print(first * second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid")
 