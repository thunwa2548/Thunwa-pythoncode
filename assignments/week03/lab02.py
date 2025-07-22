balance = 1000
pin = "1234"
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")       
        choice = input("Choose option: ")
        if choice == "1":
            print("Your balance is= ", balance)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds")
            else:
                balance -= amount
                print("{amount} withdrawn. New balance: , balance")
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                balance += amount
                print("{amount} deposited. New balance: , balance")
        elif choice == "4":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN. Access denied.")


