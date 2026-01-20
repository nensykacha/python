a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
num = input("""Select operation:
1. Addition 
2. Subtraction
3. Multiplication  
4. Division
5. Modulus
6. Exponentiation
7. Floor Division
Enter choice(1/2/3/4/5/6/7): """)


match num:
    case "1":       
        print(f"Addition of {a} and {b} is :",a+b)
    case "2":       
        print(f"Subtraction of {a} and {b} is :",a-b)
    case "3":   
        print(f"Multiplication of {a} and {b} is :",a*b)
    case "4":
        print(f"Division of {a} and {b} is :",a/b)
    case "5":
        print(f"Modulus of {a} and {b} is :",a%b)
    case "6":
        print(f"Exponentiation of {a} and {b} is :",a**b)
    case "7":
        print(f"Floor Division of {a} and {b} is :",a//b)
    case _:
        print("Invalid input")