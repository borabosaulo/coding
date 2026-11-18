while True:
    print("\n" + "=" * 45)
    print(" PYTHON TUTORIAL SYSTEM")
    print("=" * 45)
    print("1. Introduction to Programming")
    print("2. Python Basic Syntax")
    print("3. Arithmetic Operators and Expressions")
    print("4. Basic Input and Output in Python")
    print("5. Conditional Statements in Python")
    print("6. Logical Operators")
    print("7. Introduction to Iteration and Loops")
    print("0. Exit")
    print("=" * 45)

    choice = input("Choose lesson: ")

    if choice == "1":
        print("\n=== INTRODUCTION TO PROGRAMMING ===")
        print("Programming is giving instructions to a computer.")
        print("Python is a programming language.")
        print("\nExample:")
        print('print("Hello, World!")')
        print("Output: Hello, World!")

    elif choice == "2":
        print("\n=== PYTHON BASIC SYNTAX ===")
        print("Syntax refers to the rules of writing code.")
        print("\nExample:")
        print('name = "Juan"')
        print("age = 18")
        print("print(name)")
        print("Output: Juan")

    elif choice == "3":
        print("\n=== ARITHMETIC OPERATORS ===")
        print("+ Addition")
        print("- Subtraction")
        print("* Multiplication")
        print("/ Division")
        print("// Floor Division")
        print("% Modulus")
        print("** Exponentiation")
        print("\nExample:")
        print("10 + 5 = 15")
        print("10 * 5 = 50")

    elif choice == "4":
        print("\n=== BASIC INPUT AND OUTPUT ===")
        print("input() is used to receive information.")
        print("print() is used to display information.")
        print("\nExample:")
        print('name = input("Enter name: ")')
        print('print("Hello", name)')

    elif choice == "5":
        print("\n=== CONDITIONAL STATEMENTS ===")
        print("Conditional statements are used for decisions.")
        print("if - checks a condition.")
        print("elif - checks another condition.")
        print("else - executes when conditions are false.")
        print("\nExample:")
        print("age = 18")
        print("if age >= 18:")
        print(' print("Adult")')
        print("else:")
        print(' print("Minor")')

    elif choice == "6":
        print("\n=== LOGICAL OPERATORS ===")
        print("and - Both conditions must be true.")
        print("or - At least one condition must be true.")
        print("not - Reverses the condition.")
        print("\nExample:")
        print("print(5 > 2 and 10 > 5)")
        print("Output: True")

    elif choice == "7":
        print("\n=== ITERATION AND LOOPS ===")
        print("Loops are used to repeat instructions.")
        print("For loop and While loop.")
        print("\nExample:")
        print("for i in range(1, 6):")
        print(" print(i)")
        print("Output: 1 2 3 4 5")

    elif choice == "0":
        print("\nThank you for using Python Tutorial System!")
        break

    else:
        print("\nInvalid choice! Please choose only 0-7.")

    input("\nPress Enter to return to menu...")
