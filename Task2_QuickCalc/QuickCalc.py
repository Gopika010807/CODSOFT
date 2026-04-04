"""
CodSoft Internship Task
QuickCalc - Simple Calculator
Author: Gopika
"""

print("=====  QuickCalc  =====")

while True:
    try:
        # taking inputs
        n1 = float(input("\nEnter first number: "))
        n2 = float(input("Enter second number: "))

        # menu
        print("\nChoose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")

        op = input("Enter your choice: ")

        # calculation
        if op == '1' or op == '+':
            ans = n1 + n2
            print("Answer:", ans)

        elif op == '2' or op == '-':
            ans = n1 - n2
            print("Answer:", ans)

        elif op == '3' or op == '*':
            ans = n1 * n2
            print("Answer:", ans)

        elif op == '4' or op == '/':
            if n2 == 0:
                print("Cannot divide by zero!")
            else:
                ans = n1 / n2
                print("Answer:", ans)

        else:
            print("Invalid option!")

        # continue or not
        again = input("\nTry another calculation? (y/n): ")
        if again.lower() != 'y':
            print("Thanks for using QuickCalc ")
            break

    except:
        print("Invalid input! Please enter numbers only.")
