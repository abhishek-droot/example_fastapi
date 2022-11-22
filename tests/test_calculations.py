import pytest
from app.calculation import add, subtract, multiply , divide , BankAccount

@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1,num2,expected",[
   (3, 2, 5),
   (7, 1, 8),
   (12, 4, 16)
])
def testing_add(num1 , num2 , expected):
    print("testing add function")
    assert add(num1, num2) == expected
 
def test_subtract():
    assert subtract(9 , 4) == 5

def test_multiply():
    assert multiply(4,3) == 12

def test_divide():
    assert divide(20,5) == 4
 

def test_bank_set_initial_amount(bank_account):
    bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance == 0

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit():
    bank_account = BankAccount(50)
    bank_account.deposit(20)
    assert bank_account.balance == 70

def text_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 80
