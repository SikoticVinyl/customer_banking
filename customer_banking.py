# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

#Optionally adding error handling to the main function
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError(value)
            return value
        except ValueError as e:
            print(f"{e} is an invalid input. Please enter a positive number.")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError(value)
            return value
        except ValueError as e:
            print(f"{e} is an invalid input. Please enter a positive number.")

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = get_float("Enter the savings account balance: ")
    savings_interest = get_float("Enter the savings account interest rate: ")
    savings_maturity = get_int("Enter the number of months for the savings account: ")

    # Call the create_savings_account function and pass the variables from the user.
    try:
        updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
        # Print out the interest earned and updated savings account balance with interest earned for the given months.
        print(f"The interest earned on the savings account is: ${interest_earned:.2f}")
        print(f"The updated savings account balance is: ${updated_savings_balance:.2f}")
        print(f"This is the updated balance after {savings_maturity} months with an interest rate of {savings_interest}%")
    except ValueError as e:
        print(f"An error occured while processingg the savings account: {e}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = get_float("Enter the CD account balance: ")
    cd_interest = get_float("Enter the CD account interest rate: ")
    cd_maturity = get_int("Enter the number of months for the CD account: ")

    # Call the create_cd_account function and pass the variables from the user.
    try:
        updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
        # Print out the interest earned and updated CD account balance with interest earned for the given months.
        print(f"The interest earned on the CD account is: ${interest_earned:.2f}")
        print(f"The updated CD account balance is: ${updated_cd_balance:.2f}")
        print(f"This is the updated balance after {cd_maturity} months with an interest rate of {cd_interest}%")
    except ValueError as e:
        print(f"An error occured while processingg the CD account: {e}")

if __name__ == "__main__":
    main()