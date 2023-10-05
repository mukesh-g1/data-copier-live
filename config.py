import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '172.28.48.1',
            'DB_NAME': 'retail_db',
            # 'DB_USER': os.environ.get('SOURCE_DB_USER'),
            'DB_USER': 'retail_user',
            'DB_PASS': os.environ.get('SOURCE_DB_PASS'),
            'DB_PORT': 8806
        },
        'TARGET_DB': {
                    'DB_TYPE': 'postgres',
                    'DB_HOST': '172.28.48.1',
                    'DB_NAME': 'retail_db',
                    # 'DB_USER': os.environ.get('TARGET_DB_USER'),
                    'DB_USER': 'retail_user',
                    'DB_PASS': os.environ.get('TARGET_DB_PASS'),
                    'DB_PORT': 5449
                }
    }
}