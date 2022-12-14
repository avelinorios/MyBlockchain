import json

from flask import request, Flask

from infraestructure.blockchain import Blockchain
from infraestructure.converters.transaction_converter import TransactionConverter

blockchain = Blockchain()

app = Flask("api")


@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    request_body = request.json
    request_transaction = TransactionConverter().from_json(request_body)
    blockchain.add_transaction(request_transaction)
    return "Created", 201


@app.route('/mine', methods=['POST'])
def mine():
    blockchain.mine()
    return "Ok", 200


@app.route('/get_blockchain', methods=['GET'])
def get_blockchain():
    return blockchain.to_json()


if __name__ == '__main__':
    app.run(debug=True, port=9090)
