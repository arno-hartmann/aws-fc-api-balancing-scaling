import json
import os

from flask import Flask, Blueprint

api_bp = Blueprint("api", __name__)

@api_bp.route('/user/<user>')
def user(user):
    return json.dumps({"name": user})

    
@api_bp.route('/buckets')
def buckets():
    return json.dumps([{"name": "bucket1"}])

#It's me from here
# my excercise:
@api_bp.route('/s3/<bucketname>')
def bucketname(bucketname):
    
    
    return json.dumps([
        {"key": "file.txt", 
        "words": 72},
        {"key": "readme.md", 
        "words": 800}
        ])


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_bp)

    return app