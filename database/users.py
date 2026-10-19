"""User queries. All SQL is parameterized (%s), never string-formatted."""

from .connection import get_connection

def create_user(email, password_hash, name):
    '''Insert a new user. `password_hash` must already be hashed, never pass a raw password.'''

    connection = get_connection()

    with connection.cursor() as cursor:

        cursor.execute(
            '''
            INSERT INTO users (email, password_hash, name)
            VALUES (%s, %s, %s)
            ''',
            (email, password_hash, name)
        )

    connection.commit()
    connection.close()

def get_user_by_email(email):
    """Return (id, email, password_hash, name) or None if the email isn't registered. 
    
    Callers rely on this column order (e.g. signin reads the hash at index 2).
    """

    connection = get_connection()

    with connection.cursor() as cursor:

        cursor.execute(
            '''
            SELECT id, email, password_hash, name
            FROM users
            WHERE email = %s
            ''',
            (email,)
        )

        user = cursor.fetchone()

    connection.close()

    return user
