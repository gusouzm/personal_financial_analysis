"""Personal financial analysis web app (Flask).

Use create_app() to build the application; run.py is the entry point.
"""

from flask import Flask
from .routes import register_blueprints

def create_app():
    """Create and configure the Flask app, then register its blueprints."""
    # instance_relative_config: config files are looked up in instance/, not in the app folder
    app = Flask(__name__, instance_relative_config=True)

    # silent=True: a missing instance/config.py is not an error (e.g. when settings come from env vars)
    app.config.from_object('config')

    register_blueprints(app)

    return app
