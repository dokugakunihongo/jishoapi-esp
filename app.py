from flask import Flask
#from flask_cors import CORS 
from db.utils import *


#CORS(app)
def crear_app():
    app = Flask(__name__)
    
    @app.route("/search/<query>")
    def search_in_db(query):
        return Search(query)

    return app
if __name__ == "__main__":
    app = crear_app()
    app.run()