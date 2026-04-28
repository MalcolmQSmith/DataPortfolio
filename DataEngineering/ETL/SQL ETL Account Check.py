## Import needed libraries
import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

## Utlilies to configure Database credientials and database access
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": 5432,
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

SCHEMA = "analytics"
SOURCE_TABLE = "source_actuals"

TABLE_CONFIGS = [
    {
        "name": "Accounts",
        "target_table": "account_hierarchy",
        "source_key": "account_key",
        "primary_key": "account"
    },
    {
        "name": "Cost Centers",
        "target_table": "cost_center_hierarchy",
        "source_key": "cost_center_key",
        "primary_key": "cost_center_key"
    }
]

## Function that validates the both accounts between the source and target tables
def insert_new_records(cursor, cfg):
    query = sql.SQL("""
        INSERT INTO {schema}.{target} ({pk})
        SELECT DISTINCT s.{source_key}
        FROM {schema}.{source} s
        LEFT JOIN {schema}.{target} t
            ON s.{source_key} = t.{pk}
        WHERE t.{pk} IS NULL
        ON CONFLICT DO NOTHING;
    """).format(
        schema=sql.Identifier(SCHEMA),
        source=sql.Identifier(SOURCE_TABLE),
        target=sql.Identifier(cfg["target_table"]),
        source_key=sql.Identifier(cfg["source_key"]),
        pk=sql.Identifier(cfg["primary_key"]),
    )

    cursor.execute(query)

## Connects to query to run script
def run():
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            for cfg in TABLE_CONFIGS:
                insert_new_records(cursor, cfg)
        conn.commit()


if __name__ == "__main__":
    run()
