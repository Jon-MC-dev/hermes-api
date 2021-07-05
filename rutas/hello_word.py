from flask_restful import Resource


class HolaMundo(Resource):
    def get(self):
        return {'hola': 'mundo'}
