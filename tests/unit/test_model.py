from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'Italy')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.country == 'Italy'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_account_number_generation():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the account number is a 20-digit unique number
    """
    account = Account(name="Test User", currency="€", country="Italy")
    
    assert len(account.account_number) == 20  # Ensure account number is 20 digits
    assert account.account_number.isdigit()  # Ensure account number is numeric

def test_account_default_balance():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the default balance is zero
    """
    account = Account(name="Test User", currency="€", country="Spain")
    
    assert account.balance == 0.0  # Default balance should be zero

def test_account_status_default():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the default status is "Active"
    """
    account = Account(name="Test User", currency="USD", country="USA")
    
    assert account.status == "Active"  # Default status should be "Active"

def test_account_repr():
    """
    GIVEN an Account model
    WHEN the __repr__ method is called
    THEN check the output is correct
    """
    account = Account(name="Test User", currency="USD", country="USA")
    
    assert repr(account) == f"<Event '{account.account_number}'>"