import pandas as pd
from config import DB_DETAILS
from mysql import connector as mc
from mysql.connector import errorcode as ec
import psycopg2


def load_db_details(env):
    return DB_DETAILS[env]


def get_mysql_connection(db_host, db_name, db_user, db_pass, db_port):
    try:
        connection = mc.connect(user=db_user,
                                password=db_pass,
                                host=db_host,
                                database=db_name,
                                port=db_port
                                )
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        else:
            print(error)
    return connection


def get_pg_connection(db_host, db_name, db_user, db_pass, db_port):
    connection = psycopg2.connect(f"dbname={db_name} user={db_user} host={db_host} port={db_port} password={db_pass}")
    return connection


def get_connection(db_type, db_host, db_name, db_user, db_pass, db_port):
    connection = None
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host=db_host,
                                          db_name=db_name,
                                          db_user=db_user,
                                          db_pass=db_pass,
                                          db_port=db_port
                                          )
    if db_type == 'postgres':
        connection = get_pg_connection(db_host=db_host,
                                       db_name=db_name,
                                       db_user=db_user,
                                       db_pass=db_pass,
                                       db_port=db_port
                                       )
    return connection


def get_tables(path, table_list):
    tables = pd.read_csv(path, sep=':')
    if table_list == 'all':
        return tables.query('to_be_loaded == "yes"')
    else:
        table_list_df = pd.DataFrame(table_list.split(','), columns=['table_name'])
        return tables.join(table_list_df.set_index('table_name'), on='table_name', how='inner'). \
            query('to_be_loaded == "yes"')
