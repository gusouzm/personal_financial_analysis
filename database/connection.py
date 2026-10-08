import psycopg
from os import getenv

def get_connection():
    return psycopg.connect(
        host=getenv('DATABASE_HOST', 'db'),
        dbname=('DATABASE_NAME', 'personal_financial_analysis'),
        user=('DATABASE_USER', 'postgres'),
        password=('DATABASE_PASSWORD'),
        port=('DATABASE_PORT', 5432)
    )
