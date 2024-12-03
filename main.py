import pandasql as ps
from datetime import date
from DBManager import DatabaseManager
from config import get_db_url
from data import customers_data, products_data, orders_data, order_items_data

db_url = get_db_url()
db_manager = DatabaseManager(db_url)
db_manager.connect()

# db_manager.create_tables()
#
# db_manager.insert_into_table(db_manager.metadata.tables['customers'], customers_data)
# db_manager.insert_into_table(db_manager.metadata.tables['products'], products_data)
# db_manager.insert_into_table(db_manager.metadata.tables['orders'], orders_data)
# db_manager.insert_into_table(db_manager.metadata.tables['order_items'], order_items_data)




# Test
# db_manager.drop_table(table_names='order_items')
# db_manager.create_tables(table_name='order_items')






