'''Application settings, read from environment variables.

Under Docker Compose, the variables are injected by compose.yaml.
For local runs outside Docker, load_dotenv() also reads them from a .env file
(variables already set in the environment take precedence).

Required: SECRET_KEY, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD.
See .env.example for the full list.
'''

from dotenv import load_dotenv
from os import environ

load_dotenv()

SECRET_KEY = environ['SECRET_KEY']

DATABASE_NAME = environ['DATABASE_NAME']
DATABASE_USER = environ['DATABASE_USER']
DATABASE_PASSWORD = environ['DATABASE_PASSWORD']
