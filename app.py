import sys
import os
from config import DB_DETIALS

from util import get_tables


def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db_datials = DB_DETIALS[env]
    tables = get_tables('table_list')
    for table in tables['table_name']:
        print(table)

if __name__ == '__main__':
    main()
