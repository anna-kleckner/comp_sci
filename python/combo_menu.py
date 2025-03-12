def iteration_1(): 
    print("Welcome to my shop! \nWe have three types of sandwiches: Chicken ($2), Beef ($3), Tofu ($4)")
    
    sandwiches = {
        "chicken": 2,
        "beef": 3,
        "tofu": 4
    }

    user_order = input("Sandwich type: ")
    user_order = user_order.lower()

    total_price = 0
    total_price = total_price + (sandwiches[user_order])

    print(f"You ordered a {user_order} sandwich and your total is {total_price}")

#iteration_1()

def iteration_2():
    total_price = 0
    print("Welcome to my shop! \nWe have three types of sandwiches: Chicken ($2), Beef ($3), Tofu ($4)")
    
    sandwiches = {
        "chicken": 2,
        "beef": 3,
        "tofu": 4 }

    user_sandwich = input("Sandwich type: ")
    user_sandwich = user_sandwich.lower()
    total_price = total_price + (sandwiches[user_sandwich])

    beverages = {
        "small": 1,
        "medium": 1.5,
        "large": 2 }
    
    user_beverage = input("We also have beverages: small ($1), medium ($1.50), large ($2). Would you like a drink? (yes or no) ")
    if user_beverage == "yes":
        beverage = input("Beverage size: ")
        total_price = total_price + (sandwiches[user_sandwich])+ (beverages[beverage])
        print(f"You ordered a {user_sandwich} sandwich and a {beverage} beverage")
        print(f"Your total is ${total_price}")
    if user_beverage == "no":
        total_price = total_price + 0
        print(f"You ordered a {user_sandwich} sandwich")
        print(f"Your total is ${total_price}")

#iteration_2()

def iteration_3():
    total_price = 0
    print("Welcome to my shop! \nWe have three types of sandwiches: Chicken ($2), Beef ($3), Tofu ($4)")
    
    sandwiches = {
        "chicken": 2,
        "beef": 3,
        "tofu": 4 }

    user_sandwich = input("Sandwich type: ")
    user_sandwich = user_sandwich.lower()
    total_price = total_price + (sandwiches[user_sandwich])

    beverages = {
        "small": 1,
        "medium": 1.5,
        "large": 2 }

    user_beverage = input("\nWe also have beverages: small ($1), medium ($1.50), large ($2). Would you like a drink? (yes or no) ")
    if user_beverage == "yes":
        beverage = input("Beverage size: ")
        total_price = total_price + (sandwiches[user_sandwich]) + (beverages[beverage])
    if user_beverage == "no":
        total_price = total_price + 0

    fries = {
        "small": 1,
        "medium": 1.5,
        "large": 2, 
        "mega-size": 2}
    user_fry = input("\nWe also have fries: small ($1), medium ($1.50), large ($2). Would you like fries? (yes or no) ")
    if user_fry == "yes":
        fry = input("Fry size: ")
        if fry == "small":
            input("Would you like to mega-size your fries? (yes or no) ")
            if "yes":
                fry = "mega-size" 
            if "no":
                fry = "small"
    if user_fry == "no":
        total_price = total_price + 0

    if user_beverage == "yes" and user_fry == "yes":
            total_price = total_price + (sandwiches[user_sandwich]) + (beverages[beverage]) + (fries[fry])
            print(f"\nYou ordered a {user_sandwich} sandwich, a {beverage} beverage, and a {fry} fry")
            print(f"Your total is {total_price}")

    if user_beverage == "no" and user_fry == "yes":
        total_price = total_price + (sandwiches[user_sandwich]) + (fries[fry])
        print(f"\nYou ordered a {user_sandwich} sandwich and a {fry} fry")
        print(f"Your total is {total_price}")

#iteration_3()

def iteration_4():
    total_price = 0
    print("Welcome to my shop! \nWe have three types of sandwiches: Chicken ($2), Beef ($3), Tofu ($4)")
    
    sandwiches = {
        "chicken": 2,
        "beef": 3,
        "tofu": 4 }
    user_sandwich = input("Sandwich type: ")
    user_sandwich = user_sandwich.lower()
    total_price = total_price + (sandwiches[user_sandwich])

    beverages = {
        "small": 1,
        "medium": 1.5,
        "large": 2 }
    user_beverage = input("\nWe also have beverages: small ($1), medium ($1.50), large ($2). Would you like a drink? (yes or no) ")
    if user_beverage == "yes":
        beverage = input("Beverage size: ")
        total_price = total_price + (sandwiches[user_sandwich]) + (beverages[beverage])
    if user_beverage == "no":
        total_price = total_price + 0

    fries = {
        "small": 1,
        "medium": 1.5,
        "large": 2, 
        "mega-size": 2}
    user_fry = input("\nWe also have fries: small ($1), medium ($1.50), large ($2). Would you like fries? (yes or no) ")
    if user_fry == "yes":
        fry = input("Fry size: ")
        if fry == "small":
            input("Would you like to mega-size your fries? (yes or no) ")
            if "yes":
                fry = "mega-size" 
            if "no":
                fry = "small"
    if user_fry == "no":
        total_price = total_price + 0
    
    ketchup = int(input("How many ketchup packets would you like? (0+) "))
    
    if user_beverage == "yes" and user_fry == "yes":
            total_price = total_price + (sandwiches[user_sandwich]) + (beverages[beverage]) + (fries[fry]) + (0.5 * ketchup) - 1
            print(f"\nYou ordered a {user_sandwich} sandwich, a {beverage} beverage, and a {fry} fry")
            print(f"Your total is {total_price}")

    if user_beverage == "no" and user_fry == "yes":
        total_price = total_price + (sandwiches[user_sandwich]) + (fries[fry]) + (0.5 * ketchup)
        print(f"\nYou ordered a {user_sandwich} sandwich and a {fry} fry")
        print(f"Your total is {total_price}")

    if user_beverage == "yes" and user_fry == "no":
        total_price = total_price + (sandwiches[user_sandwich]) + (beverages[beverage]) + (0.5 * ketchup)
        print(f"\nYou ordered a {user_sandwich} sandwich and a {beverage} beverage")
        print(f"Your total is {total_price}")

    if user_beverage == "no" and user_fry == "no":
        total_price = total_price + (sandwiches[user_sandwich]) + (0.5 * ketchup)
        print(f"\nYou ordered a {user_sandwich} sandwich")
        print(f"Your total is ${total_price:.2f}")

iteration_4()