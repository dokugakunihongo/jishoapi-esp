from flask import Flask
#from flask_cors import CORS 
from db.utils import *

app = Flask(__name__)
#CORS(app)

@app.route("/search/<query>")
def search_in_db(query):
    return Search(query)