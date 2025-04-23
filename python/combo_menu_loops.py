def user_order():
    total_price = 0
    user_order = []

    print("\nWe have three types of sandwiches: Chicken ($2), Beef ($3), Tofu ($4)")
    
    sandwiches = {
        "chicken": 2,
        "beef": 3,
        "tofu": 4 }
    user_sandwich = str(input("Sandwich type: "))
    user_order.append(user_sandwich)

    beverages = {
        "small": 1,
        "medium": 1.5,
        "large": 2 }
    user_beverage = str(input("\nWe also have beverages: small ($1), medium ($1.50), large ($2). Would you like a drink? (yes or no) "))
    if user_beverage == "yes":
        beverage = str(input("Beverage size: "))
        user_order.append(beverage)
    elif user_beverage == "no":
        total_price = total_price + 0
    
    fries = {
        "small": 1,
        "medium": 1.5,
        "large": 2, 
        "mega-size": 2}
    user_fry = str(input("\nWe also have fries: small ($1), medium ($1.50), large ($2). Would you like fries? (yes or no) "))
    if user_fry == "yes":
        fry = str(input("Fry size: "))
        user_order.append(fry)
        if fry == "small":
            str(input("Would you like to mega-size your fries? (yes or no) "))
            if "yes":
                fry = "mega-size"
                user_order[2] = 'large'
                user_order.append('mega-size')
            if "no":
                fry = "small"
                user_order.append(fry)
    if user_fry == "no":
        total_price = total_price + 0
    
    ketchup = int(input("How many ketchup packets would you like? (0+) "))
    
    if user_beverage == "yes" and user_fry == "yes":
        total_price = total_price + (sandwiches[user_sandwich]) + (beverages[beverage]) + (fries[fry]) + (0.5 * ketchup) - 1
        print(f"\nYou ordered a {user_order[0]} sandwich, a {user_order[1]} beverage, and a {user_order[2]} fry")
        print(f"Your total is ${total_price:.2f}")

    if user_beverage == "no" and user_fry == "yes":
        total_price = total_price + (sandwiches[user_sandwich]) + (fries[fry]) + (0.5 * ketchup)
        print(f"\nYou ordered a {user_order[0]} sandwich and a {user_order[1]} fry")
        print(f"Your total is ${total_price:.2f}")

    if user_beverage == "yes" and user_fry == "no":
        total_price = total_price + (sandwiches[user_sandwich]) + (beverages[beverage]) + (0.5 * ketchup)
        print(f"\nYou ordered a {user_order[0]} sandwich and a {user_order[1]} beverage")
        print(f"Your total is ${total_price:.2f}")

    if user_beverage == "no" and user_fry == "no":
        total_price = total_price + (sandwiches[user_sandwich]) + (0.5 * ketchup)
        print(f"\nYou ordered a {user_order[0]} sandwich")
        print(f"Your total is ${total_price:.2f}")

def main():
    print("Welcome to my shop!")
    user_order()
   
    order_again = str(input(f"\nWould you like to order agin? (yes or no) "))
    while order_again == "yes":
        user_order()
        order_again = str(input(f"\nWould you like to order agin? (yes or no) "))
    if order_again != "yes":
        print(f"\nThank you for coming to my shop!")

main()