class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f'Owner: {self.owner}, Current balance: {self.balance}$.'

    def add_money(self, amount_: float) -> None:
        self.balance += amount_

    def sub_money(self, amount_: float) -> None:
        self.balance -= amount_

    def check_balance(self) -> None:
        print(self)


name: str = input("Enter owner name: ")
while True:
    try:
        tem_balance: float = float(input('Enter your balane: '))
        break
    except ValueError:
        print('You need to enter float number.')
account: BankAccount = BankAccount(name, tem_balance)
while True:
    try:
        choice: int = int(input('''Do you want do some balance operation?
1 - Deposit money
2 - Take money
3 - Check balance
4 - Exit program\n'''))
        match choice:
            case 1:
                while True:
                    try:
                        amount: float = float(input('Enter the amount of money you want to put on the card: '))
                        account.add_money(amount)
                        break
                    except ValueError:
                        print('You need to enter float nuber.')
            case 2:
                while True:
                    try:
                        amount: float = float(input('Enter the amount of money you want to take from the card: '))
                        if amount > account.balance:
                            print('You do not have enough money.')
                        else:
                            account.sub_money(amount)
                        break
                    except ValueError:
                        print('You need to enter float nuber.')
            case 3:
                account.check_balance()
            case 4:
                print('Program finished.')
                break
            case _:
                print('Incorrect data.')
    except ValueError:
        print('You need to enter integer number.')
