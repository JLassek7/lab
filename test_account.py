import pytest
from account import *

class Test:
    def setup_method(self):
        self.account1 = Account('Justin')
        self.account2 = Account('Tom')
        self.account1.deposit(100)
        self.account2.deposit(50.50)
    
    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'Justin'
        assert self.account2.get_name() == 'Tom'
        assert self.account1.get_balance() == 100
        assert self.account2.get_balance() == 50.50
    
    def test_deposit(self):
        assert self.account1.deposit(23.50) == True
        assert self.account1.deposit(0) == False
        assert self.account1.deposit(-10.25) == False

        assert self.account2.deposit(12) == True
        assert self.account2.deposit(0) == False
        assert self.account2.deposit(-5.23) == False

    def test_withdraw(self):
        assert self.account1.withdraw(15.23) == True
        assert self.account1.withdraw(0.00) == False
        assert self.account1.withdraw(-12.3) == False
        assert self.account1.withdraw(200) == False

        assert self.account2.withdraw(25) == True
        assert self.account2.withdraw(0) == False
        assert self.account2.withdraw(-12.00) == False
        assert self.account2.withdraw(75) == False

if __name__ == "__main__":
    pytest.main()