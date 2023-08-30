class ATM:
    def __init__(self):
        self.denominations = [500, 200, 50]

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount for withdrawal.")
            return

        remaining_amount = amount
        notes_count = {}

        for denomination in self.denominations:
            if remaining_amount >= denomination:
                count = remaining_amount // denomination
                notes_count[denomination] = count
                remaining_amount %= denomination

        if remaining_amount == 0:
            print("Withdrawal successful. Breakdown of notes:")
            for denomination, count in notes_count.items():
                print(f"{denomination} notes: {count}")
        else:
            print("Unable to dispense the requested amount with available denominations.")

    def run(self):
        while True:
            try:
                amount = int(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

            choice = input("Do you want to continue (C) or cancel (X)? ").strip().lower()
            if choice != 'c':
                print("Transaction canceled.")
                break


# Instantiate the ATM class and run the program
atm_machine = ATM()
atm_machine.run()
