# Customer Banking System

This project involves creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

## Challenge Instructions

### Create the Savings Account Function

1. Open the `savings_account.py` file.
2. Import the `Account` class from the `Accounts.py` file.
3. In the `create_savings_account` function, do the following:
   - Create an instance of the `Account` class and pass in the balance and interest parameters.
   - Calculate the interest earned.
   - Update the savings account balance by adding the interest earned.
   - Pass the updated balance to the `set_balance` method using the instance of the `Account` class.
   - Pass the interest earned to the `set_interest` method using the instance of the `Account` class.
   - Return the updated balance and interest earned.

### Create the CD Account Function

1. Open the `cd_account.py` file.
2. Import the `Account` class from the `Accounts.py` file.
3. In the `create_cd_account` function, do the following:
   - Create an instance of the `Account` class and pass in the balance and interest parameters.
   - Calculate the interest earned.
   - Update the CD account balance by adding the interest earned.
   - Pass the updated balance to the `set_balance` method using the instance of the `Account` class.
   - Pass the interest earned to the `set_interest` method using the instance of the `Account` class.
   - Return the updated balance and interest earned.

### Create the Main Function

1. Open the `customer_banking.py` file.
2. Import the `create_cd_account` and `create_savings_account` functions from the appropriate files.
3. In the main function, do the following:
   - Prompt the user to set the savings balance, interest rate, and months for the savings account.
   - Call the `create_savings_account` function and pass in the variables from the user.
   - Print out the interest earned and updated savings account balance with interest earned for the given months.
   - Prompt the user to set the CD balance, interest rate, and months for the CD account.
   - Call the `create_cd_account` function and pass the variables from the user.
   - Print out the interest earned and updated CD account balance with interest earned for the given months.
   - Call the main function.

## Hints and Considerations

- Consider creating one Python file that has all the functions first, then separate the functions into different files.
- Look back on some of the activities you did in class.
- Use pseudocoding to help you write out the steps.
- Always commit your work and back it up with pushes to GitHub or GitLab.
- Ensure that your repo has a detailed README.md file.

## Requirements

### Create the Savings Account Function (35 points)

- The `Account` class from the `Accounts.py` file is imported. (4 points)
- In the `create_savings_account` function, an instance of the `Account` class is created and the balance and interest parameters are passed to the `Account` class. (6 points)
- The interest earned is calculated and assigned to a variable. (4 points)
- The savings account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)
- The updated balance is passed to the `set_balance` method using the instance of the `Account` class. (6 points)
- The interest earned is passed to the `set_interest` method using the instance of the `Account` class. (6 points)
- The updated balance and interest earned are returned by the function. (5 points)

### Create the CD Account Function (35 points)

- The `Account` class from the `Accounts.py` file is imported. (4 points)
- In the `create_cd_account` function, an instance of the `Account` class is created and the balance and interest parameters are passed to the `Account` class. (6 points)
- The interest earned is calculated and assigned to a variable. (4 points)
- The CD account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)
- The updated balance is passed to the `set_balance` method using the instance of the `Account` class. (6 points)
- The interest earned is passed to the `set_interest` method using the instance of the `Account` class. (6 points)
- The updated balance and interest earned are returned by the function. (5 points)

### Create the Main Function (30 points)

- The user is prompted to set the savings balance, interest rate, and months for the savings account. (8 points)
- Code is written to print out the interest earned and updated savings account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)
- The user is prompted to set the CD balance, interest rate, and months for the CD account. (8 points)
- Code is written to print out the interest earned and updated CD account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)
- The main function is called to run the program. (2 points)
