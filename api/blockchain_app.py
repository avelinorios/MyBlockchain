from flask import Flask
from infraestructure.blockchain import Blockchain

blockchain = Blockchain()
app = Flask(__name__)

