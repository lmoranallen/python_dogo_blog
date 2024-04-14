from flask import Flask

from .config import app_config

def create_app(env):
    """
    Create new app
    """

    app = Flask(__name__)

    app.config.from_object(app_config[env])

    @app.route('/', methods=['GET'])
    def index():
        """
        pseudo endpoint
        """
        return 'Hello World successful.'
    return app