import sys
from util import get_tables, load_db_details
from read import read_table
from write import load_table


def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables = get_tables('table_list')
    table_name = 'departments'
    for table_name in tables['table_name']:
        print(f'reading data for {table_name}')
        data, column_names = read_table(db_details=db_details, table_name=table_name)
        print(f'loading data for {table_name}')
        load_table(db_details=db_details, data=data, column_names=column_names, table_name=table_name)


if __name__ == '__main__':
    main()
