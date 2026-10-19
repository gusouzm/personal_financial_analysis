"""Route blueprints (auth, homepage) and their registration."""

from .auth import auth
from .homepage import homepage

def register_blueprints(app):
    """Attach every blueprint to `app`. Add new blueprints here, with their URL prefix."""
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(homepage, url_prefix='/homepage')
