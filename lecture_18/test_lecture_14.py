from lecture_14.task_3 import Account, SavingsAccount, CurrentAccount, Bank
import pytest


@pytest.mark.parametrize(
    "account_number, expected_number ,expected_balance, deposit, expected_result, withdraw, expected_withdraw", [
        ("123", "123", 0, 123, 123, 10, 113),
        (123, 123, 0, 406, 406, 300, 106),
        ('SAA123', 'SAA123', 0, 134223, 134223, 134223, 0),
        ('231SAA', '231SAA', 0, 12, 12, 13, -1),
        ('saa', 'saa', 0, 0, False, 0, None),
        ('/:$#', '/:$#', 0, -1, False, 0, None)
    ])
def test_account_functionality(account_number, expected_number, expected_balance, deposit, expected_result, withdraw,
                               expected_withdraw):
    test_account = Account.create_account(account_number)
    assert test_account.get_account_number() == expected_number
    assert test_account.get_balance() == expected_balance
    if not expected_result:
        with pytest.raises(ValueError):
            test_account.deposit(deposit)
    else:
        test_account.deposit(deposit)
        assert test_account.get_balance() == expected_result
    if expected_withdraw == None:
        with pytest.raises(ValueError):
            test_account.withdraw(withdraw)
    else:
        test_account.withdraw(withdraw)
        assert test_account.get_balance() == expected_withdraw


# Test SavingsAccount and CurrentAccount

@pytest.mark.parametrize("balance, account_number, interest, expected_interest", [
    (100, 'sam', 15, 115),
    (1000, '123', 1, 1010.00),
    (0, '45', 3, 0),
    (5, 'p1233', -2, 4.90),
    (5000, 'perry', 30, 6500.00),
    (30, 1222, 20, 36),
])
def test_savings_account(balance, account_number, interest, expected_interest):
    test_account = SavingsAccount(balance, account_number, interest)
    assert test_account.get_balance() == balance
    assert test_account.get_account_number() == account_number
    test_account.add_interest()
    assert test_account.get_balance() == expected_interest


@pytest.mark.parametrize("balance, account_number, overdraft, withdraw, expected_balance", [
    (100, 'sam', 100, 200, -100),
    (1000, '123', 300, 100, 900),
    (0, '45', 0, 1000, False),
])
def test_savings_account(balance, account_number, overdraft, withdraw, expected_balance):
    test_account = CurrentAccount(balance, account_number, overdraft)
    assert test_account.get_balance() == balance
    if expected_balance == False:
        with pytest.raises(ValueError):
            test_account.check_over(withdraw)
    else:
        test_account.check_over(withdraw)
        assert test_account.get_balance() == expected_balance


# Test Bank

@pytest.mark.parametrize("balance, account_number, interest, expected_interest", [
    (100, 'sam', 15, 115),
    (1000, '123', 1, 1010.00),
    (0, '45', 3, 0),
])
def test_bank_saving(balance, account_number, interest, expected_interest):
    test_account = Account(balance, account_number)
    bank = Bank()
    bank.open_account(test_account)
    assert len(bank.accounts) == 1
    for account in bank.accounts:
        assert account.get_balance() == balance
        bank.remove_account_by_id(account.get_account_number())
    assert len(bank.accounts) == 0


