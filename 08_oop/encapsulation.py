# Encapsulation in Python

class BankAccount:
    """A class demonstrating encapsulation principles"""
    
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder  # Protected attribute
        self.__balance = initial_balance      # Private attribute
        self.__transaction_log = []           # Private attribute
    
    # Public methods
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            self.__log_transaction("deposit", amount)
            return True
        return False
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__log_transaction("withdrawal", amount)
            return True
        return False
    
    def get_balance(self):
        """Public method to check balance"""
        return self.__balance
    
    def get_account_info(self):
        """Public method to get account information"""
        return {
            "holder": self._account_holder,
            "balance": self.__balance,
            "transactions": len(self.__transaction_log)
        }
    
    # Private method
    def __log_transaction(self, transaction_type, amount):
        """Private method to log transactions"""
        self.__transaction_log.append({
            "type": transaction_type,
            "amount": amount
        })
    
    # Property decorators
    @property
    def account_holder(self):
        """Getter for account holder"""
        return self._account_holder
    
    @account_holder.setter
    def account_holder(self, value):
        """Setter for account holder"""
        if len(value) >= 2:
            self._account_holder = value
        else:
            raise ValueError("Account holder name must be at least 2 characters")

# Using the BankAccount class
if __name__ == "__main__":
    # Create account
    account = BankAccount("John Doe", 1000)
    
    # Using public methods
    print("Initial account info:")
    print(account.get_account_info())
    
    # Make some transactions
    account.deposit(500)
    account.withdraw(200)
    
    print("\nUpdated account info:")
    print(account.get_account_info())
    
    # Using property
    print(f"\nAccount holder: {account.account_holder}")
    account.account_holder = "Jane Doe"
    print(f"New account holder: {account.account_holder}")
    
    # Demonstrating encapsulation
    try:
        # This will raise an AttributeError
        print(account.__balance)
    except AttributeError as e:
        print(f"\nCan't access private attribute: {e}")
    
    # Name mangling still allows access (but don't do this!)
    print("\nAccessing private attribute through name mangling:")
    print(account._BankAccount__balance)
    
    try:
        # This will raise a ValueError
        account.account_holder = "A"
    except ValueError as e:
        print(f"\nValidation error: {e}") 