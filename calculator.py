def calculator():
    print("=== Simple Calculator ===")
    
    num1 = float(input("Pehla number daalo: "))
    num2 = float(input("Doosra number daalo: "))
    
    print("\nOperation chunao:")
    print("1. Jama (+)")
    print("2. Minus (-)")
    print("3. Zarb (*)")
    print("4. Taqseem (/)")
    
    choice = input("1/2/3/4 daalo: ")
    
    if choice == "1":
        result = num1 + num2
        print(f"\nJawab: {num1} + {num2} = {result}")
        
    elif choice == "2":
        result = num1 - num2
        print(f"\nJawab: {num1} - {num2} = {result}")
        
    elif choice == "3":
        result = num1 * num2
        print(f"\nJawab: {num1} * {num2} = {result}")
        
    elif choice == "4":
        if num2 == 0:
            print("\nGalti! Zero se taqseem nahi ho sakti!")
        else:
            result = num1 / num2
            print(f"\nJawab: {num1} / {num2} = {result}")
    else:
        print("\nGalat option!")

calculator()