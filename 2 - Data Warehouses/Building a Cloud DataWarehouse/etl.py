# to check s3 bucket at console, append bucket name to: https://s3.console.aws.amazon.com/s3/buckets/

import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection):
    """
    Copy data from S3 into redshift's staging tables
    
    Args:
        cur: cursor the execute queries
        conn: connection to the database. Used to commit queries
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection):
    """
    Insert data from staging tables into redshift's tables
    
    Args:
        cur: cursor the execute queries
        conn: connection to the database. Used to commit queries
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print('Connecting to datawarehouse...')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print('Connected')
    
    print('Loading S3 to stage tables...')
    load_staging_tables(cur, conn)
    print('Loaded')
    print('Insert data into normal tables...')
    insert_tables(cur, conn)
    print('Finished!')

    conn.close()


if __name__ == "__main__":
    main()