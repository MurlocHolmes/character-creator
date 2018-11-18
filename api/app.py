from flask import Flask
from flask_restplus import Resource, Api
from flask_cors import CORS
import utils


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/universe'
CORS(app)
api = Api(app, version='1.0', title='Universe API',
          description='API for Universe', )
utils.connect(app)


from characters.routes import api as character_api  # noqa
from universe.routes import api as universe_api  # noqa
from locations.routes import api as location_api  # noqa
from items.routes import api as item_api  # noqa
api.add_namespace(character_api)
api.add_namespace(universe_api)
api.add_namespace(location_api)
api.add_namespace(item_api)
# utils.db.create_all()
# utils.db.session.commit()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
