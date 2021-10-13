from flask import Flask
from flask_restful import Api
from resources.chaves_ied import Chaves_ied, Chave_ied

app = Flask(__name__)
api = Api(app)

api.add_resource(Chaves_ied, '/chaves_ied')
api.add_resource(Chave_ied, '/chaves_ied/<string:chave_id>')
#api.add_resource(Chaves_ied, '/chaves_ied/<string:IED>')

if __name__ == '__main__':
    app.run(debug=True)
