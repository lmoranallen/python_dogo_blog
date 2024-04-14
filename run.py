import os

from src.app import create_app

if __name__ == '__main__':
    env = os.getenv('FLASK_ENV')
    app = create_app(env)
    app.run()