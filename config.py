'''Application settings, read from environment variables.

Under Docker Compose, the variables are injected by compose.yaml.
For local runs outside Docker, load_dotenv() also reads them from a .env file
(variables already set in the environment take precedence).

Required: SECRET_KEY, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD.
See .env.example for the full list.
'''

from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
