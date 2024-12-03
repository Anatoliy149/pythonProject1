from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, ForeignKey, Float, insert, \
    inspect, text
from sqlalchemy.exc import SQLAlchemyError


class DatabaseManager:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.metadata = MetaData()

        self.customers_table = Table(
            'customers', self.metadata,
            Column('customer_id', Integer, primary_key=True),
            Column('name', String, nullable=False),
            Column('email', String, unique=True),
            Column('registration_date', Date)
        )

        self.products_table = Table(
            'products', self.metadata,
            Column('product_id', Integer, primary_key=True),
            Column('name', String, nullable=False),
            Column('category', String),
            Column('price', Float)
        )

        self.orders_table = Table(
            'orders', self.metadata,
            Column('order_id', Integer, primary_key=True),
            Column('customer_id', ForeignKey('customers.customer_id')),
            Column('order_date', Date),
            Column('status', String)
        )

        self.order_items_table = Table(
            'order_items', self.metadata,
            Column('order_item_id', Integer, primary_key=True),
            Column('order_id', ForeignKey('orders.order_id')),
            Column('product_id', ForeignKey('products.product_id')),
            Column('quantity', Integer)
        )

    # Функция для подключения к БД
    def connect(self):
        try:
            with self.engine.connect() as conn:
                print('Подключение к БД прошло успешно')
                return conn
        except Exception as e:
            print(f"Ошибка подключения к БД - {e}")

    # Функция для создания таблиц
    def create_tables(self, table_name=None):
        # Создаем только указанную таблицу
        if table_name:
            table = self.metadata.tables.get(table_name)
            if table is None:
                print(f'Таблица {table_name} не найдена в метаданных. Создание не выполнено')
                return
            table.create(self.engine)
            print(f'Таблица {table_name} успешно создана')
        # Создаем все таблицы
        else:
            self.metadata.create_all(self.engine)
            print('Таблицы успешно созданы')

    # Функция для заполнения таблиц данными
    def insert_into_table(self, table_name: Table, data: list[dict]):
        try:
            with self.engine.begin() as conn:
                conn.execute(insert(table_name), data)
                print(f'Данные успешно вставлены в таблицу {table_name}')
        except SQLAlchemyError as e:
            print(f'Ошибка при вставке данных в таблицу - {e}')

    # Функция для удаления таблицы или списка таблиц
    def drop_table(self, table_names):
        if isinstance(table_names, str):
            table_names = [table_names]

        inspector = inspect(self.engine)
        existing_tables = inspector.get_table_names()

        for table_name in table_names:
            if table_name in existing_tables:
                table = self.metadata.tables.get(table_name)
                if table is not None:
                    with self.engine.connect() as conn:
                        try:
                            table.drop(self.engine)
                            print(f"Таблица {table_name} удалена.")
                        except Exception as e:
                            print(f"Ошибка при удалении таблицы {table_name}: {e}")
            else:
                print(f"Таблица {table_name} не найдена в БД. Удаление не выполнено.")

    # Функция для чтения и выполнения sql файла
    def execute_sql_file(self, file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read().strip()

            with self.engine.connect() as conn:
                result = conn.execute(text(sql_script))
                rows = result.fetchall()
                print(f'SQL скрипт из файла {file_path} выполнен')
                return rows

        except Exception as e:
            print(f'Ошибка при выполнении скрипта из файла {file_path}: {e}')
            return None
