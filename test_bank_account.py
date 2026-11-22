import pytest
from bank_account import BankAccount


def test_new_account_starts_with_zero():
    account = BankAccount("Sara")
    assert account.get_balance() == 0


def test_new_account_with_starting_balance():
    account = BankAccount("Sara", 100)
    assert account.get_balance() == 100


def test_negative_starting_balance_raises_error():
    with pytest.raises(ValueError):
        BankAccount("Sara", -5)


def test_deposit_increases_balance():
    account = BankAccount("Sara", 100)
    account.deposit(50)
    assert account.get_balance() == 150


def test_deposit_zero_raises_error():
    account = BankAccount("Sara", 100)
    with pytest.raises(ValueError):
        account.deposit(0)


def test_deposit_negative_raises_error():
    account = BankAccount("Sara", 100)
    with pytest.raises(ValueError):
        account.deposit(-20)


def test_withdraw_decreases_balance():
    account = BankAccount("Sara", 100)
    account.withdraw(30)
    assert account.get_balance() == 70


def test_withdraw_all_money():
    account = BankAccount("Sara", 100)
    account.withdraw(100)
    assert account.get_balance() == 0


def test_withdraw_more_than_balance_raises_error():
    account = BankAccount("Sara", 100)
    with pytest.raises(ValueError):
        account.withdraw(500)


def test_withdraw_negative_raises_error():
    account = BankAccount("Sara", 100)
    with pytest.raises(ValueError):
        account.withdraw(-10)
