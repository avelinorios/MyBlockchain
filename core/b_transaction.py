

class Transaction:
    """
    Contains the representation of a money transaction.
    :param  sender: the address that is the origin of the transaction.
    :param receiver: the address that receives the money.
    :param amount: the quantity of money.
    """
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def create_transaction(self, sender, receiver, amount):
        self.__init__(sender, receiver, amount)
