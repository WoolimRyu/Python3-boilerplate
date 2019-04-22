from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)


class CreateBot(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('config', type=str)
            args = parser.parse_args()

            _id = args['id']
            _config = args['config']

            return {'botId': _id, 'config': _config}
        except Exception as e:
            return {'error': str(e)}


api.add_resource(CreateBot, '/bot')

if __name__ == '__main__':
    app.run(debug=True)
