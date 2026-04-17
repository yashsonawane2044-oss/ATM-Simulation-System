pin = "1234"
balance = 5000

user_pin = input("Enter PIN: ")

if user_pin == pin:

    while True:
        print("\n1.Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        ch = input("Enter Choice: ")

        if ch == "1":
            print("Balance =", balance)

        elif ch == "2":
            amount = int(input("Enter Amount: "))
            balance = balance + amount
            print("Deposited")

        elif ch == "3":
            amount = int(input("Enter Amount: "))

            if amount <= balance:
                balance = balance - amount
                print("Take Cash")
            else:
                print("No Balance")

        elif ch == "4":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

else:
    print("Wrong PIN")