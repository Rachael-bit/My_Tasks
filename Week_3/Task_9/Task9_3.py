# Creating a bank ussd for ACE bank
# Get started 
secret = "*100#"

while True:
    start = input("Dail *10# to get started: ").title()
    if start == secret:
         print("Welcome to ACE bank!!!")
         break
    else:
         print("Wrong code! Dial *100#.")

balance = 50000
while True:
    print("\nMain Menu:") # welcome message 
    print("1. Check Balance")
    print("2. Bank Transfer")
    print("0. Exit")

    choice = input("Enter option: ")

    if choice == "1":
        print(f"Your balance is: N{balance}")
        continue

    elif choice == "2":
        print("\nTransfer Menu: ")
        print("1. ACE Bank")
        print("2. GTB Bank")
        print("3. OPAY Bank")
        print("0. END89")
    elif choice == "0":
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid option. Try again.")
        continue

    option = input("Enter Your Option: ")
        
    if option in ["1", "2", "3"]:
            account_number = input("Enter recipient's account number: ")
            account_name = input("Enter account name: ")
            amount = int(input("Enter amount to transfer: "))
            if amount <=balance:
                balance -= amount
                print(f"N{amount} was successfully transferred to {account_name}. New balance: N{balance}")
            else:
                print("Insufficient funds.")
    elif option == "0":
            print(f"Thank you for banking with us.")
            break
    else:
            print("Invalid Option. Try again.")
        
