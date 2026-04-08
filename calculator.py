def calculator():
    print("=== Simple Calculator ===")
    
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    print("\nOperation chose:")
    print("1. add (+)")
    print("2. sub (-)")
    print("3. multi (*)")
    print("4. div (/)")
    
    choice = input("1/2/3/4 add: ")
    
    if choice == "1":
        result = num1 + num2
        print(f"\nanswer: {num1} + {num2} = {result}")
        
    elif choice == "2":
        result = num1 - num2
        print(f"\nAnswer: {num1} - {num2} = {result}")
        
    elif choice == "3":
        result = num1 * num2
        print(f"\nAnswer: {num1} * {num2} = {result}")
        
    elif choice == "4":
        if num2 == 0:
            print("\nwronge! Zero se taqseem nahi ho sakti!")
        else:
            result = num1 / num2
            print(f"\nAnswer: {num1} / {num2} = {result}")
    else:
        print("\nwronge option!")

calculator()