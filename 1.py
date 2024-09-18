def calculate_amount(total_units, user_type):
    if user_type == 1:  # House_hold
        amount = total_units * 4.8
        final = amount + amount * 0.18
        total_amount = final + 25
    elif user_type == 2:  # Small_industries
        amount = total_units * 4
        final = amount + amount * 0.18
        total_amount = final + 60
    elif user_type == 3:  # Factories
        amount = total_units * 3.2
        final = amount + amount * 0.18
        total_amount = final + 200
    else:
        raise ValueError("Invalid user type")
    
    return amount, final, total_amount

def main():
    print("    KP Electric Distributors  ")
    
    try:
        total_units = int(input("Enter the number of units: "))
        user_type = int(input("Select type: 1: House_hold, 2: Small_industries, 3: Factories: "))

        amount, final, total_amount = calculate_amount(total_units, user_type)

        print("\nTotal amount to be paid:")
        print(f"Amount (without tax): ${amount:.2f}")
        print(f"Amount (with tax): ${final:.2f}")
        print(f"Total to be paid (incl. additional charges): ${total_amount:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")

main()
