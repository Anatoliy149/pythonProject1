from DBManager import DatabaseManager
from config import get_db_url
import matplotlib.pyplot as plt
import seaborn as sns


db_url = get_db_url()
db_manager = DatabaseManager(db_url)
db_manager.connect()

"""
# 6) Построить гистограмму, показывающая количество заказов по каждому клиенту.
res_6 = db_manager.execute_sql_file(file_path='query.sql')
print(res_6)

names = [row[0] for row in res_6]
order_counts = [row[1] for row in res_6]

# Строим гистограмму через seaborn
sns.barplot(x=names, y=order_counts)
plt.title("Количество заказов по клиентам", fontsize=16)
plt.xlabel("Клиенты", fontsize=14)
plt.ylabel("Количество заказов", fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.show()
"""

# 7) График топ-5 самых популярных товаров

res_7 = db_manager.execute_sql_file(file_path='query.sql')
print(res_7)

products = [row[0] for row in res_7]
quantity_products = [row[1] for row in res_7]

# Строим график через seaborn
sns.lineplot(x=products, y=quantity_products)
plt.title("Топ-5 самых популярных товаров", fontsize=16)
plt.xlabel("Товары", fontsize=14)
plt.ylabel("Количество проданных товаров", fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.show()
