class Account:
    """
    This class represents a bank account
    """
    def __init__(self, name: str) -> None:
        '''
        Constructor for bank account objects
        :param name: Name of the bank account
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Mutator function, adds the amount passed into the funciton if the amount is greater than 0
        :param amount: amount to be added to the bank account, must be greater than 0
        :return: T or F, whether the deposit worked or not
        """
        if amount <= 0:
            return False
        else:    
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Mutator method, subtracts the amount passed into the function from the balance 
        if the amount is greater than 0 and less than the current balance.
        :param amount: the amount to be subtracted from the bank account. Must be greater than 0 and less then the current balance.
        :return: T or F, whether the withdraw was successful or not
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Getter method, retrieves the current balance.
        :return: name of the account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Getter method, retrieves the account name 
        :return: name of the account
        """
        return self.__account_name