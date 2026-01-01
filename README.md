# ATM-MANAGEMENT-SYSTEM-BY-USING-PYTHON

#Project Overview
The ATM Management System is a console-based mini project developed using Python and Object-Oriented Programming (OOPS) principles.
This project simulates real-world ATM operations such as checking balance, depositing money, withdrawing cash, and viewing account details.
The main goal of this project is to understand how real-world banking systems can be modeled using classes, objects, inheritance, encapsulation, abstraction, and polymorphism in Python.

# Key Objectives

--> Understand core OOPS concepts through a practical project

--> Build a menu-driven application using loops

--> Implement secure data handling using encapsulation

--> Simulate real ATM functionalities in a simple way

# Technologies Used

Language: Python
Concepts: Object-Oriented Programming (OOPS), Abstraction, Encapsulation, Inheritance, Polymorphism, Class Methods and Static Methods

# OOPS Concepts Implemented

🔹Abstraction:
    Implemented using an abstract base class BankAccount
    Forces child class to implement the transaction() method

🔹Encapsulation:
    Secure data handling using:
        Public variables
        Protected variables (_account_number)
        Private variables (__balance, __pin)
    Getter and setter methods used for controlled access

🔹Inheritance:
    ATM class inherits from:
        Account
        BankAccount

🔹Polymorphism:
    Method overriding of transaction() in the child class

🔹 Instance, Class & Static Methods
      Instance Methods: deposit_money(), withdraw_money(), check_balance()
      Class Method: Display bank name (same for all users)
      Static Method: Validate transaction amounts

# Features:
✔ Check account balance
✔ Deposit money
✔ Withdraw money (with validation & limits)
✔ View account details
✔ PIN verification for security
✔ Transaction history tracking
✔ Transaction count
✔ Exit confirmation
✔ Menu-driven interface

# Security Features:
✔ PIN authentication before accessing ATM
✔ Encapsulation of sensitive data
✔ Withdrawal validation
✔ Maximum withdrawal limit

# How to Run the Project:

---> Step 1: Install Python 3. Download from https://www.python.org/downloads/
---> Step 2: Download this file
---> Step 3: Navigate the folder
---> Step 4: Run the code python (filename).py

# Sample Output

WELCOME TO ABC BANK ATM

Enter Account Holder Name: Rahul
Enter Account Number: 12345
Enter Initial Balance: 1000
Set a 4-digit PIN: ****

Enter PIN to access ATM: ****

Deposit Successful!
Updated Balance: ₹1500

# Future Enhancements

--> Add database support (MySQL / SQLite)
--> Support for multiple user accounts
--> GUI-based application using Tkinter
--> Web-based version using Flask/Django
--> Detailed transaction logs with date & time
--> Integration with real banking APIs
--> Advanced error handling & logging

# Learning Outcomes

--> Strong understanding of Object-Oriented Programming
--> Hands-on experience with real-world system modeling
--> Improved logical thinking and Python skills
--> Better understanding of secure data handling

# Conclusion

This project successfully demonstrates how an ATM system can be designed using Python and OOPS concepts.
It is beginner-friendly, well-structured, and serves as a solid foundation for advanced backend or full-stack projects.
