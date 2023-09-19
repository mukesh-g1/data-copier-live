import sys
import os
from config import DB_DETIALS


def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db_datials = DB_DETIALS[env]
    print(db_datials)


if __name__ == '__main__':
    main()
