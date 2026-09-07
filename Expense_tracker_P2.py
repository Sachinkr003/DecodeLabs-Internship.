total = 0.0

while True:
    user_input = input("Enter expense amount (or type 'quit' to finish): ")

    if user_input.lower() == "quit":
        break

    try:
        expense = float(user_input)
        total += expense
    except ValueError:
        print("Invalid Data. Please enter a valid number.")

print(f"Final Total: ₹{total:.2f}")