'''Vityarthi Project
A Savings and Expense Manager
Made by Akshat Garg 25BCE10693
Class: Introduction To Problem Solving
Faculty: Dr. Saravanan D
Slot: B11 + B12 + B13 '''


import datetime

transactions = []

print("== Savings and Expense Manager ==")
# Gives the user options to choose
while True:
    print("1. Add Transaction")
    print("2. List Recent Transactions")
    print("3. Check Balance")
    print("4. Set Monthly Savings")
    print("5. Exit")
    

      
    Selection = (input("Select an Option: "))
    # Inputs the option from the user

    if Selection == "1":
        try:
            amount = int(input("Enter amount to deposit: "))
            description = input("Enter a description (e.g Groceries, Gas etc.)")
            current_date = datetime.datetime.now()

            new_transaction = {
                "amount": amount,
                "description": description,
                "date": current_date
            }

            transactions.append(new_transaction)

            print(f"Transaction for '{description}', '{amount}' added successfully")
               
        except ValueError:
            print("Invalid amount, Please enter a number.")
            
    elif Selection == "2":
        print("== Recent Transactions ==")
        if not transactions:
            print("No transactions recorded yet. Select option 1  to add one.")

        else:
            for transaction in (transactions):
                print(f"{transaction['description']}: {transaction['amount']:}")     
                
    elif Selection == "3": 
        print("== Current Balance ==")
        if not transactions:
            print("No transactions yet. Balance is 0.")
        else:
            balance = sum(t["amount"] for t in transactions)
            print(f"Your current balance is: {balance}")
    
    elif Selection == "4":
        print("== Monthly Savings ==")
        # Ask for saving goal
        while True:
            goal_input = input("Enter your saving goal amount (e.g. 5000 or 2500.50): ").strip()
            try:
                goal = float(goal_input)
                if goal <= 0:
                    print("Goal must be greater than 0. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number like 1000 or 1234.56.")

        # Ask for months to achieve goal
        while True:
            months_input = input("In how many months do you want to achieve this goal? (integer): ").strip()
            try:
                months = int(months_input)
                if months <= 0:
                    print("Months must be a positive integer. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number of months, e.g. 6 or 12.")

        # Calculate monthly amount to save
        monthly_needed = goal / months
        # Optional: show integer representation for cases where transactions use int
        print("== Savings Plan ==")
        print(f"Goal: {goal:}")
        print(f"Months to achieve: {months}")
        print(f"You need to save {monthly_needed:} per month to reach the goal in {months} months.")
            
    elif Selection == "5":
        print("Bye!")
        break
    else:
        print("Invalid option, please select an option from the menu")




