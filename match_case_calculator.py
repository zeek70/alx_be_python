num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
operation=input("Choose the operation (+, -, *, /):.")
match operation :
    case "+":
        result = num1 + num2
        print("The result is ",result)
    case "*":
        result = num1 - num2
        print("The result is ",result)
    case "-":
        result = num1 * num2
        print("The result is ",result)
    case "/":
        result = num1 / num2
        if num2==0:
           printrint("Cannot divide by zero.")
        else:
            print("The result is ",result)
    case _:
        print("invalid entry")
