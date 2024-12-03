def get_db_url():
    user = 'postgres'
    password = 'postgres'
    host = 'localhost'
    port = 5432
    database = 'alchemy'

    return f"postgresql://{user}:{password}@{host}:{port}/{database}"
