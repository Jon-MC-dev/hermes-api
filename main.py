from flask import Flask
from flask_restful import Api

from rutas.hello_word import HolaMundo

app = Flask(__name__)
api = Api(app)

api.add_resource(HolaMundo, '/')

if __name__ == '__main__':
    app.run(debug=True)