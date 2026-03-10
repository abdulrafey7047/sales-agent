import psycopg2
import constants

from psycopg2.extras import RealDictCursor


def get_db_connection():
    """Helper to create a fresh connection to Postgres."""
    return psycopg2.connect(
        host=constants.DB_HOST,
        database=constants.DB_NAME,
        user=constants.DB_USER,
        password=constants.DB_PASSWORD,
        port=constants.DB_PORT
    )


def execute_insert(table: str, row_data: dict):
    """Generic Insert logic with better error handling."""
    if not row_data:
        raise ValueError("No data provided for insertion")

    columns = list(row_data.keys())
    values = [row_data[column] for column in columns]
    column_names = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(values))
    query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, tuple(values))
            conn.commit()


def execute_select(table: str, col: str, val: str):
    """Generic Select logic."""
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            query = f"SELECT * FROM {table} WHERE {col} = %s"
            cur.execute(query, (val,))
            result = cur.fetchone()
            return dict(result) if result else None
