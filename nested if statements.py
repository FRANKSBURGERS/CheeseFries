def calculate_bonus():
    name = input("Enter Employee Name: ")
    shifts = int(input("Enter number of shifts: "))
    transactions = int(input("Enter number of transactions: "))
    transaction_value = float(input("Enter transactions dollar value: "))

    if transactions == 0 or shifts == 0:
        print("Invalid input: Number of transactions and shifts must be greater than 0.")
        return

    average_transaction_value = transaction_value / transactions
    productivity_score = average_transaction_value / shifts

    if productivity_score <= 30:
        bonus = 50.0
    elif productivity_score <= 69:
        bonus = 75.0
    elif productivity_score <= 199:
        bonus = 100.0
    else:
        bonus = 200.0

    print(f"Employee Name: {name}")
    print(f"Employee Bonus: ${bonus:.1f}")

calculate_bonus()
