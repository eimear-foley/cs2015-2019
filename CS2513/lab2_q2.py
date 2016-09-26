from random import choice

def createId():

    """Creates a six character ID for the account holder
    through random assignment of digits between 0 and 9 and lowercase letters"""

    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = [n for n in range(10)]
    account_id = ''
    for _ in range(3):
        account_id += str(choice(letters))
        account_id += str(choice(numbers))
        
    return account_id
    
class BankAccount(object):

    """BankAccount is a class defined by the following instance variables:
         - name of the account holder
         - unique six character ID
         - balance of account"""

    def __init__(self, name):
        self._name = name
        self._account_id = createId()
        self._balance = 0

    def __str__(self):

        """String Representation of the instance variables of the class i.e.
           Account Holder, Account ID, Balance."""

        descriptive_str = ("Account Holder: %s - Account ID: %s - Balance: %i" % (self._name, self._account_id, self._balance))
        return descriptive_str

    @property
    def balance(self):

        """Returns the bank balance of the account holder."""
        return ('Balance: %i' % (self._balance))

    @balance.setter 
    def balance(self, balance):

        """Sets bank balance to amount specified by user."""

        if balance > 0:
            self._balance = balance
            print('Balance: %i' % (self._balance))
        else:
            print('Please enter a valid value.')

    @property
    def account_id(self):

        """Returns the account ID of the account holder."""
        return ('Account ID: %s' % (self._account_id))

    @property
    def name(self):

        """Returns the name of the account holder."""
        return ('Account Holder: %s' % (self._name))

    def creditAccount(self, amount):

        """A method by which the balance of the account holder can be increased."""

        if amount >= 0:
            self._balance += amount
            return('Your account has increased by %i. Balance: %i' % (amount, self._balance))
        else:
            return('Please enter a valid value.')

    def debitAccount(self, amount):

        """A method by which the balance of the account holder can be decreased."""

        if amount >= 0:
            self._balance -= amount
            return('Your account has decrease by %i. Balance: %i' % (amount, self._balance))
        else:
            return('Please enter a valid value.')

def main():

    """Test block which is execute only when the module is run, not when it is imported."""

    bank_account1 = BankAccount('Eimear')
    print(bank_account1)

    bank_account1.balance = 50
    print(bank_account1)

    print(bank_account1.balance)
    print(bank_account1.account_id)
    print(bank_account1.name)

    print(bank_account1.creditAccount(40))
    print(bank_account1.debitAccount(10))
        
        
if __name__ == '__main__':
    main()
    
