# 🏦 ATM and Bank Account Simulator

A menu-driven ATM and Bank Account Simulator developed using Python. This project demonstrates basic banking operations, cash dispensing, transaction management, file handling, and important Python programming concepts.

## 📌 Project Overview

**Project:** ATM and Bank Account Simulator  
**Project Number:** 3  
**Group:** Group 3

### Group Members
- Eklavya Tyagi
- Ashish Kumar
- Manish Kumar
- Sumit Raj

## 🎯 Objective

To develop a Python program that simulates the basic operations of an Automated Teller Machine (ATM), allowing users to securely access a sample bank account, perform transactions, and maintain transaction records.

## ✨ Features

- **PIN Authentication:** Login with a maximum of three attempts.
- **Balance Enquiry:** Check the current account balance.
- **Deposit Money:** Add money to the account.
- **Withdraw Money:** Withdraw money with an insufficient-balance check.
- **Cash Dispensing:** Automatically calculate the number of notes required using denominations of ₹2000, ₹500, ₹200, and ₹100.
- **Mini Statement:** Display the latest five transactions.
- **File Handling:** Save and load account details and transaction history using a `.txt` file.
- **Compound Interest:** Calculate compound interest using recursion.
- **Input Validation:** Handle invalid inputs and prevent the program from crashing.

## 🛠️ Technologies and Concepts Used

### Technology
- Python 3
- Visual Studio Code (for development)

### Python Concepts Demonstrated

| Concept | Application |
|---|---|
| Variables and Data Types | Store account information and transaction amounts |
| Strings | Handle PIN input and transaction descriptions |
| Operators | Perform calculations and comparisons |
| Lists | Maintain transaction history |
| `append()` | Add new transactions |
| `remove()` | Remove processed denominations from a working list |
| Slicing | Display the latest five transactions |
| `sort()` | Arrange denominations in descending order |
| Sets | Store unique cash denominations |
| Tuples | Store transactions as `(type, amount)` |
| Dictionaries | Store account details |
| Conditional Statements | Validate inputs and control menu operations |
| For and While Loops | Process transactions and run the ATM menu |
| Nested Loops | Calculate the number of notes required |
| Functions | Organize the program into reusable operations |
| Recursion | Calculate compound interest |
| File Handling | Save and load account information |
| Exception Handling | Handle invalid input and file errors |
| Doctests | Test functions using embedded examples |

## 📂 Project Structure

```text
ATM-Bank-Account-Simulator/
│
├── atm-bank-project.py
│
├── bank_data.txt
│
└── README.md
```

- `atm-bank-project.py` – Main Python source code containing all ATM operations.
- `bank_data.txt` – Stores account details and transaction history.
- `README.md` – Project documentation.

## ⚙️ Installation and Execution

### Prerequisites

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.

No external libraries or database systems are required.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Open the Project Folder

```bash
cd ATM-Bank-Simulator
```

### Step 3: Run the Program

```bash
python atm-bank-project.py
```

The program will automatically load the saved account data. If the data file does not exist, it will create one using the initial account information.

## 🔐 Sample Login Details

The following are the initial demonstration credentials:

| Detail | Value |
|---|---|
| Bank Name | Python Bank |
| Account Number | 1001 |
| Account Holder | Ashish |
| Initial PIN | 1234 |
| Initial Balance | ₹20,000 |

**Note:** These are sample credentials for demonstration purposes only.

## 📋 ATM Menu

After successful authentication, the following menu is displayed:

```text
========== ATM MENU ==========

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Mini Statement
5. Calculate Compound Interest
6. Exit
```

Select an option to perform the corresponding operation.

## 💵 Cash Dispensing Logic

The simulator uses four denominations:

- ₹2000
- ₹500
- ₹200
- ₹100

It uses a nested-loop approach:
1. The outer `for` loop visits each denomination in descending order.
2. The inner `while` loop counts how many notes of that denomination are needed.
3. The remaining withdrawal amount is reduced after each note is counted.

**Example:**

For a withdrawal of ₹4700:

| Denomination | Number of Notes |
|---|---:|
| ₹2000 | 2 |
| ₹500 | 1 |
| ₹200 | 1 |
| ₹100 | 0 |

Total = ₹4700

## 🔄 Data Persistence

The program uses a plain-text file named `bank_data.txt` to preserve account details and transaction history.

- Account information is loaded when the program starts.
- Successful deposits and withdrawals are saved automatically.
- All transactions are preserved in the file.
- The mini statement displays only the latest five transactions.
- Account information is saved again when the user exits.

The data file is stored in the same folder as the Python source file.

## 🧮 Compound Interest Using Recursion

The project includes a recursive function to calculate compound interest over a given number of years.

**Formula:**

\[
A = P\left(1+\frac{R}{100}\right)^T
\]

Where:

- `P` = Principal amount
- `R` = Annual interest rate
- `T` = Number of years
- `A` = Final amount

The recursive function calculates one year's growth at a time and uses a base case when the remaining number of years becomes zero.

## 🧪 Testing

The project includes doctest examples in at least three functions.

To run the tests, execute:

```bash
python atm-bank-project.py
```

The program runs its doctests before starting the ATM simulator.

Important test cases include:

- Correct and incorrect PIN authentication.
- Maximum three login attempts.
- Valid and invalid deposits.
- Successful withdrawals.
- Insufficient balance handling.
- Cash denomination calculation.
- Mini statement displaying the latest five transactions.
- Data persistence after restarting the program.
- Compound interest calculation.
- Handling invalid numeric input.

## ⚠️ Limitations

- The project uses a single sample bank account.
- Account information is stored locally in a text file.
- The PIN is stored as plain text and is not suitable for real banking security.
- The cash dispensing calculation assumes the listed denominations are available.
- The project is designed for educational purposes and is not connected to an actual banking system.

## 🚀 Future Improvements

Possible improvements include:
- Support for multiple bank accounts.
- Better account authentication and PIN security.
- More detailed transaction reports.
- Additional ATM operations.
- Backup and recovery of account data.

## 🎓 Conclusion

The ATM and Bank Account Simulator demonstrates how fundamental Python programming concepts can be applied to a practical banking scenario. It combines data structures, loops, nested loops, functions, recursion, file handling, exception handling, and doctests in a single menu-driven application.

This project provides practical experience in problem-solving, program design, data management, and Python programming.

---

**Developed by Group 3**  
**Project 3 – ATM and Bank Account Simulator**