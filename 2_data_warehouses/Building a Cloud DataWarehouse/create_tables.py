import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection) -> None:
    """
    Drop all tables

    Args:
        cur: cursor the execute queries
        conn: connection to the database. Used to commit queries
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection) -> None:
    """
    Create all needed tables

    Args:
        cur: cursor the execute queries
        conn: connection to the database. Used to commit queries
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print('Connecting to datawarehouse...')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Connected')
    cur = conn.cursor()

    print('Dropping existing tables...')
    drop_tables(cur, conn)
    print('Dropped tables')
    print('Creating new tables...')
    create_tables(cur, conn)
    print('Created new tables')

    conn.close()


if __name__ == "__main__":
    main()
