import random
import string

def generate_password():
    print("--- Random Password Generator ---")
    
    try:
        # Step 1: Get password length from the user
        length = int(input("Enter the desired length of the password (e.g., 12): "))
        
        if length <= 0:
            print("Error: Password length must be greater than zero.")
            return

        # Step 2: Define character pools (Letters, Digits, Symbols)
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Step 3: Ask for user preferences (Optional customization)
        print("\nChoose complexity options:")
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower()
        use_digits = input("Include numbers? (y/n): ").strip().lower()
        use_symbols = input("Include special symbols? (y/n): ").strip().lower()

        # Combine character pool according to user choices
        character_pool = lower  # Lowercase letters are always included
        if use_upper == 'y':
            character_pool += upper
        if use_digits == 'y':
            character_pool += digits
        if use_symbols == 'y':
            character_pool += symbols

        # Step 4: Generate password by selecting random characters
        password = "".join(random.choice(character_pool) for _ in range(length))

        # Step 5: Display the final password
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Error: Please enter a valid numeric value for the length.")

if __name__ == "__main__":
    generate_password()