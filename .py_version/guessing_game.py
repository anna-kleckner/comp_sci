def get_secret_number():
    while True:
        try:
            secret_number = int(input(f"\nEnter the secret number here: "))
            if secret_number <= 0:
                print("Number must be a whole number great than 0")
                continue
            else:
                break
        except: 
            print("Number must be a whole number great than 0")
            continue
    return secret_number

def main():
    secret_number = get_secret_number()
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n")

    inncorrect_guesses = 0
    while True:             
        try:
            user_guess = int(input("\nGuess: "))
            if user_guess == secret_number: 
                print("\nDING DING DING")
                break                
            elif user_guess > secret_number:
                print(f"Lower \nGuesses left: {2-inncorrect_guesses}")
                inncorrect_guesses = inncorrect_guesses + 1
                if inncorrect_guesses == 3:
                    print(f"\nThe correct answer is: {secret_number}")
                    break  
            elif user_guess < secret_number:
                print(f"Higher \nGuesses left: {2-inncorrect_guesses}")
                inncorrect_guesses = inncorrect_guesses + 1
                if inncorrect_guesses == 3:
                    print(f"\nThe correct answer is: {secret_number}")
                    break               
            else: 
                 break
        except:
            print("Incorrect")                
            inncorrect_guesses = inncorrect_guesses + 1
            if inncorrect_guesses == 3:
                print(f"Correct answer is: {secret_number}")
                break
main()