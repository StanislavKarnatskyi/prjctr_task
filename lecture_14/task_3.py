class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self):
        self._balance = self._balance + (self._balance * (self.interest / 100))

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance:.2f}'



class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft):
        super().__init__(balance, account_number)
        self.overdraft = overdraft

    def check_over(self, minus):
        if (self._balance - minus) < -self.overdraft:
            raise ValueError(f'Denied. {self._account_number} limit overdraft.')
        else:
            self._balance -= minus

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance:.2f}'



class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def remove_account_by_id(self, account_id):
        self.accounts = [account for account in self.accounts if account.get_account_number() != account_id]

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.check_over(150)

