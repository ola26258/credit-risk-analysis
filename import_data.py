import psycopg2
import os
from psycopg2 import OperationalError

# Параметры подключения - ЗАМЕНИТЕ НА СВОИ
DB_PARAMS = {
    "dbname": "credit_risk",      # Имя вашей БД
    "user": "postgres",           # Имя пользователя (по умолчанию 'postgres')
    "password": "123",     # Ваш пароль от PostgreSQL
    "host": "localhost",          # Если БД не локальная, укажите IP/домен
    "port": "5432"                # Порт (по умолчанию 5432)
}

def import_data():
    try:
        # Подключение к БД
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        
        # Полный путь к папке со скриптом
        base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Пути к файлам
        loans_path = os.path.join(base_path, 'data', 'loans.csv')
        customers_path = os.path.join(base_path, 'data', 'customers.csv')
        
        # Проверка существования файлов
        if not os.path.exists(loans_path):
            raise FileNotFoundError(f"Файл {loans_path} не найден")
        if not os.path.exists(customers_path):
            raise FileNotFoundError(f"Файл {customers_path} не найден")
        
        # Импорт данных
        with open(loans_path, 'r', encoding='utf-8') as f:
            cur.copy_expert("COPY loans FROM STDIN WITH CSV HEADER DELIMITER ','", f)
            print(f"Импортировано данных в loans: {cur.rowcount} строк")
        
        with open(customers_path, 'r', encoding='utf-8') as f:
            cur.copy_expert("COPY customers FROM STDIN WITH CSV HEADER DELIMITER ','", f)
            print(f"Импортировано данных в customers: {cur.rowcount} строк")
        
        conn.commit()
        print("Данные успешно импортированы!")
        
    except OperationalError as e:
        print(f"Ошибка подключения к PostgreSQL: {e}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        conn.rollback()
        print(f"Произошла ошибка: {e}")
    finally:
        if 'conn' in locals():
            cur.close()
            conn.close()

if __name__ == "__main__":
    import_data()
    input("Нажмите Enter для выхода...")  # Чтобы окно не закрывалось сразу