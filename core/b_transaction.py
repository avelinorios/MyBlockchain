import json


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

    def __repr__(self):
        return f"sender: {self.sender}, receiver: {self.receiver}, amount: {self.amount}"

    def create_transaction(self, sender, receiver, amount):
        self.__init__(sender, receiver, amount)

    @property
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
