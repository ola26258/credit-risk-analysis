import pandas as pd
import numpy as np
from datetime import date

# Настройка случайных значений для воспроизводимости
np.random.seed(42)

# Параметры генерации
NUM_CUSTOMERS = 1000  # Количество клиентов
NUM_LOANS = 5000      # Количество кредитов

# Генерация данных клиентов
def generate_customers(num_customers):
    regions = ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Kazan']
    data = {
        'customer_id': np.arange(100, 100 + num_customers),
        'income': np.random.randint(30000, 200000, size=num_customers),
        'employment_length': np.random.randint(1, 10, size=num_customers),
        'region': np.random.choice(regions, size=num_customers),
    }
    return pd.DataFrame(data)

# Генерация данных по кредитам
def generate_loans(num_loans, num_customers):
    loan_types = ['personal', 'mortgage', 'auto', 'business']
    statuses = ['active', 'default', 'paid', 'late']
    credit_bands = ['300-500', '500-600', '600-700', '700+']
    
    data = {
        'loan_id': np.arange(1, num_loans + 1),
        'customer_id': np.random.randint(100, 100 + num_customers, size=num_loans),
        'loan_amount': np.random.randint(10000, 5000000, size=num_loans),
        'loan_type': np.random.choice(loan_types, size=num_loans, p=[0.4, 0.3, 0.2, 0.1]),
        'interest_rate': np.round(np.random.uniform(5, 25, size=num_loans), 1),
        'term': np.random.choice([12, 24, 36, 60, 120], size=num_loans),
        'issue_date': pd.to_datetime([date(2020, 1, 1) + pd.Timedelta(days=np.random.randint(0, 1000)) for _ in range(num_loans)]),
        'status': np.random.choice(statuses, size=num_loans, p=[0.6, 0.1, 0.25, 0.05]),
        'credit_score_band': np.random.choice(credit_bands, size=num_loans, p=[0.2, 0.3, 0.3, 0.2]),
    }
    
    # Расчет EAD и recovered_amount для дефолтов
    df = pd.DataFrame(data)
    df['exposure_at_default'] = df['loan_amount'] * np.random.uniform(0.8, 1.2, size=num_loans)
    df['recovered_amount'] = np.where(
        df['status'] == 'default',
        df['exposure_at_default'] * np.random.uniform(0.1, 0.7),  # Возвращают 10-70% при дефолте
        0  # Для не-дефолтных кредитов
    )
    return df

# Генерация и сохранение данных
customers = generate_customers(NUM_CUSTOMERS)
loans = generate_loans(NUM_LOANS, NUM_CUSTOMERS)

# Сохранение в CSV
customers.to_csv('data/customers.csv', index=False)
loans.to_csv('data/loans.csv', index=False)

print(f"Данные сгенерированы:\n- customers.csv: {len(customers)} записей\n- loans.csv: {len(loans)} записей")
input("Нажмите Enter для выхода...")  # Окно не закроется, пока вы не нажмете Enter