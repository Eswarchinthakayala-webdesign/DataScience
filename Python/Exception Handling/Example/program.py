try:
    num1=int(input("Enter the Number: "))
    num2 = int(input("Enter the Number: "))

    result=num1/num2
    print("Result: ",result)
except ZeroDivisionError:
    print(f"Division by zero not accept")
