"""Auth blueprint: sign-in and sign-up routes."""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import signin
from . import signup
