from core.b_transaction import Transaction


class TransactionConverter:
    """
    Transform dato to Transaction object
    """

    def from_json(self, json_data) -> Transaction:
        self.validate_json(json_data)
        return Transaction(json_data['sender'], json_data['receiver'], json_data['amount'])

    def validate_json(self, json_data):
        if not json_data['sender'] or json_data['sender'] is None:
            raise Exception('Sender is not valid.')
        if not json_data['receiver'] or json_data['receiver'] is None:
            raise Exception('Receiver is not valid.')
        if not json_data['amount'] or json_data['amount'] is None:
            raise Exception('Amount is not valid.')

