print("Welcome to Habib Metro! Please Enter your card to continue")

balance = 7500  # initial balance
pin = "1234"  # user pin

def authenticate_pin():
    attempts = 0
    while attempts < 3:
        user_pin = input("Enter your pin number :")
        if user_pin == pin:
            return True
        else:
            print("Invalid pin number. Please try again.")
            attempts += 1
    return False

def display_menu():
    print("Welcome to Habib Metro!")
    print("Please select an option from the menu below:")
    return input("1:Check Balance \n2:Withdraw \n3:Deposit \n4:Exit \n")

def check_balance():
    print(f"Your current balance is:${balance}")

def withdraw_amount():
    global balance
    while True:
        try:
            withdraw = int(input("Enter the amount you want to withdraw:"))
            if withdraw > balance:
                print("Insufficient balance")
            else:
                balance -= withdraw
                print(f"Your withdrawal Amount is ${withdraw}")
                print(f"Your new balance is:${balance}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def deposit_amount():
    global balance
    while True:
        try:
            deposit = int(input("Enter the amount you want to deposit:"))
            balance += deposit
            print(f"Your deposit Amount is ${deposit}")
            print(f"Your new balance is:${balance}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    if authenticate_pin():
        while True:
            choice = display_menu()
            if choice == "1":
                check_balance()
            elif choice == "2":
                withdraw_amount()
            elif choice == "3":
                deposit_amount()
            elif choice == "4":
                print("Thank you for using Habib Metro!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()