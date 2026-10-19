"""Database connection helper.

Reads the DATABASE_* environment variables. Under Docker Compose they come
from compose.yaml; outside Docker they must be exported (or loaded from .env) first.
"""

import psycopg
from os import getenv, environ

def get_connection():
    """Open a new connection on every call. The caller is responsible for closing it."""

    return psycopg.connect(
        host=getenv('DATABASE_HOST', 'db'), # harmless default: 'db' is the Compose service name.
        port=getenv('DATABASE_PORT', '5432'), # harmless default: Postgres standard port.
        dbname=environ['DATABASE_NAME'], # required: raises KeyError if missing.
        user=environ['DATABASE_USER'], # required: never fall back to a superuser.
        password=environ['DATABASE_PASSWORD']
    )
