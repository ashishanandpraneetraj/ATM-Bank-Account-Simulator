
# ==========================================
# PROJECT 3: ATM AND BANK ACCOUNT SIMULATOR
# GROUP 3
# ==========================================


# ==========================================
# 1. FILE LOCATION
# ==========================================

# Create bank_data.txt in the same folder as this Python file.
# No additional module is required.

DATA_FILE = __file__.replace(
    "atm-bank-project.py",
    "bank_data.txt"
)


# ==========================================
# 2. INITIAL DATA
# ==========================================

bank_details = ("Python Bank", "ATM Simulator")

account = {
    "account_number": 1001,
    "account_holder": "Ashish",
    "pin": 1234,
    "balance": 20000
}

transactions = [
    ("Deposit", 5000),
    ("Withdrawal", 2000),
    ("Deposit", 1000)
]

denominations = {2000, 500, 200, 100}


# ==========================================
# 3. PIN AUTHENTICATION
# ==========================================

def authenticate(account):

    attempts = 0

    while attempts < 3:

        entered_pin = input("Enter your 4-digit PIN: ").strip()

        if entered_pin == str(account["pin"]):

            print("\nLogin successful!")
            return True

        else:

            attempts += 1

            print("Incorrect PIN!")

            if attempts < 3:
                print("Attempts remaining:", 3 - attempts)

    print("\nYour account is locked.")

    return False


# ==========================================
# 4. CHECK BALANCE
# ==========================================

def check_balance(account):
    """
    >>> check_balance({"balance": 20000})
    20000

    >>> check_balance({"balance": 5000})
    5000
    """

    return account["balance"]


# ==========================================
# 5. RECORD TRANSACTIONS
# ==========================================

def record_transaction(transactions, transaction_type, amount):

    # Store every transaction as a tuple.
    transactions.append((transaction_type, amount))


# ==========================================
# 6. DEPOSIT MONEY
# ==========================================

def deposit(account, transactions, amount):
    """
    >>> a = {"balance": 1000}
    >>> t = []
    >>> deposit(a, t, 500)
    True
    >>> a["balance"]
    1500
    >>> deposit(a, t, 0)
    False
    """

    if amount <= 0:

        return False

    account["balance"] += amount

    record_transaction(transactions, "Deposit", amount)

    return True


# ==========================================
# 7. CASH DISPENSING
# ==========================================

def dispense_cash(amount, denominations):
    """
    >>> dispense_cash(4700, {2000, 500, 200, 100})
    [(2000, 2), (500, 1), (200, 1), (100, 0)]

    >>> dispense_cash(300, {2000, 500, 200, 100})
    [(2000, 0), (500, 0), (200, 1), (100, 1)]
    """

    # Convert the set into a list.
    notes = list(denominations)

    # Arrange notes from largest to smallest.
    notes.sort(reverse=True)

    # Make a working copy for processing.
    remaining_notes = notes[:]

    remaining = amount

    breakdown = []

    # Outer loop: process each note denomination.
    for note in notes:

        count = 0

        # Inner loop: count how many notes are required.
        while remaining >= note:

            count += 1

            remaining -= note

        breakdown.append((note, count))

        # Remove the denomination after processing it.
        remaining_notes.remove(note)

    if remaining != 0:

        return None

    return breakdown


# ==========================================
# 8. WITHDRAW MONEY
# ==========================================

def withdraw(account, transactions, amount):

    if amount <= 0:

        print("Invalid withdrawal amount.")

        return False

    if amount > account["balance"]:

        print("Insufficient balance!")

        return False

    if amount % 100 != 0:

        print("Amount must be a multiple of 100.")

        return False

    breakdown = dispense_cash(amount, denominations)

    if breakdown is None:

        print("Cash cannot be dispensed.")

        return False

    account["balance"] -= amount

    record_transaction(transactions, "Withdrawal", amount)

    print("\nCash dispensed successfully!")

    print("Notes provided:")

    for note, count in breakdown:

        if count > 0:

            print("Rs.", note, "x", count)

    return True


# ==========================================
# 9. MINI STATEMENT
# ==========================================

def mini_statement(transactions):

    print("\n================================")
    print("         MINI STATEMENT")
    print("================================")

    # Display only the latest five transactions.
    recent_transactions = transactions[-5:]

    if len(recent_transactions) == 0:

        print("No transactions available.")

        return

    print("\nTransaction Type       Amount")

    print("--------------------------------")

    for transaction in recent_transactions:

        transaction_type = transaction[0]

        amount = transaction[1]

        print(transaction_type, "          Rs.", amount)

    print("--------------------------------")

    print("Total transactions displayed:", len(recent_transactions))


# ==========================================
# 10. SAVE DATA TO TEXT FILE
# ==========================================

def save_data(account, transactions):

    with open(DATA_FILE, "w") as file:

        # Save account details, one value per line.
        file.write(str(account["account_number"]) + "\n")

        file.write(account["account_holder"] + "\n")

        file.write(str(account["pin"]) + "\n")

        file.write(str(account["balance"]) + "\n")

        # Save the total number of transactions.
        file.write(str(len(transactions)) + "\n")

        # Save every transaction.
        for transaction in transactions:

            transaction_type = transaction[0]

            amount = transaction[1]

            file.write(transaction_type + "|" + str(amount) + "\n")

    print("Account data saved successfully.")


# ==========================================
# 11. LOAD DATA FROM TEXT FILE
# ==========================================

def load_data(account, transactions):

    try:

        with open(DATA_FILE, "r") as file:

            lines = file.readlines()

        # Read and validate account details.
        account_number = int(lines[0].strip())

        account_holder = lines[1].strip()

        pin = int(lines[2].strip())

        balance = int(lines[3].strip())

        transaction_count = int(lines[4].strip())

        if transaction_count < 0 or len(lines) != 5 + transaction_count:
            raise ValueError("Invalid transaction data.")

        # Read transactions into a temporary list first.
        loaded_transactions = []

        for line in lines[5:]:

            transaction_type, amount = line.strip().split("|", 1)

            loaded_transactions.append(
                (transaction_type, int(amount))
            )

        # Update the account only after successful reading.
        account["account_number"] = account_number

        account["account_holder"] = account_holder

        account["pin"] = pin

        account["balance"] = balance

        transactions.clear()

        for transaction in loaded_transactions:

            transactions.append(transaction)

        print("Previous account data loaded successfully.")

    except FileNotFoundError:

        print("No previous data found.")

        save_data(account, transactions)

    except (ValueError, IndexError):

        print("Saved data is invalid. Using initial account data.")

        save_data(account, transactions)


# ==========================================
# 12. COMPOUND INTEREST USING RECURSION
# ==========================================

def compound_interest(principal, rate, years):
    """
    Calculate compound interest recursively.

    >>> compound_interest(1000, 10, 1)
    1100.0

    >>> compound_interest(1000, 10, 0)
    1000
    """

    # Base condition.
    if years == 0:

        return principal

    # Calculate the amount after one year.
    new_amount = principal * (1 + rate / 100)

    # Recursive call.
    return compound_interest(new_amount, rate, years - 1)


# ==========================================
# 13. MAIN ATM PROGRAM
# ==========================================

def main():

    # Load previous account information.
    load_data(account, transactions)

    print("\n========================================")

    print("          ", bank_details[0])

    print("          ", bank_details[1])

    print("========================================")

    # Check customer PIN.
    if authenticate(account):

        print("\nAccount Holder:", account["account_holder"])

        while True:

            print("\n========== ATM MENU ==========")

            print("1. Check Balance")

            print("2. Deposit Money")

            print("3. Withdraw Money")

            print("4. Mini Statement")

            print("5. Calculate Compound Interest")

            print("6. Exit")

            choice = input("\nEnter your choice: ").strip()


            # ----------------------------------
            # OPTION 1: CHECK BALANCE
            # ----------------------------------

            if choice == "1":

                balance = check_balance(account)

                print("\nYour current balance is: Rs.", balance)


            # ----------------------------------
            # OPTION 2: DEPOSIT MONEY
            # ----------------------------------

            elif choice == "2":

                try:

                    amount = int(input("Enter deposit amount: "))

                    if deposit(account, transactions, amount):

                        print("\nDeposit successful!")

                        print("New balance:", account["balance"])

                        save_data(account, transactions)

                    else:

                        print("Invalid deposit amount.")

                except ValueError:

                    print("Please enter a valid number.")


            # ----------------------------------
            # OPTION 3: WITHDRAW MONEY
            # ----------------------------------

            elif choice == "3":

                try:

                    amount = int(input("Enter withdrawal amount: "))

                    if withdraw(account, transactions, amount):

                        print("\nWithdrawal successful!")

                        print("New balance:", account["balance"])

                        save_data(account, transactions)

                except ValueError:

                    print("Please enter a valid number.")


            # ----------------------------------
            # OPTION 4: MINI STATEMENT
            # ----------------------------------

            elif choice == "4":

                mini_statement(transactions)


            # ----------------------------------
            # OPTION 5: COMPOUND INTEREST
            # ----------------------------------

            elif choice == "5":

                try:

                    principal = float(input("Enter principal amount: "))

                    rate = float(input("Enter annual interest rate: "))

                    years = int(input("Enter number of years: "))

                    if principal <= 0 or rate < 0 or years < 0:

                        print("Please enter valid values.")

                    else:

                        final_amount = compound_interest(
                            principal, rate, years
                        )

                        interest = final_amount - principal

                        print(
                            "\nFinal Amount: Rs.",
                            round(final_amount, 2)
                        )

                        print(
                            "Compound Interest: Rs.",
                            round(interest, 2)
                        )

                except ValueError:

                    print("Please enter valid numeric values.")


            # ----------------------------------
            # OPTION 6: EXIT
            # ----------------------------------

            elif choice == "6":

                save_data(account, transactions)

                print("\nThank you for using Python Bank!")

                break


            # ----------------------------------
            # INVALID MENU CHOICE
            # ----------------------------------

            else:

                print("\nInvalid choice. Please try again.")

    else:

        print("\nAccess denied. Please contact the bank.")


# ==========================================
# 14. PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":

    import doctest

    print("\nRunning Doctests...")

    doctest.testmod(verbose=True)

    print("\nStarting ATM Simulator...")

    main()








