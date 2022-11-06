from flask import request, Flask

from infraestructure.blockchain import Blockchain
from core.b_transaction import Transaction
from infraestructure.converters.transaction_converter import TransactionConverter

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    request_body = request.form
    request_transaction = TransactionConverter.from_json(request_body)
    blockchain.add_transaction(request_transaction)


if __name__ == "__main__":
    app.run(debug=True, port=9090)
