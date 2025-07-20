# credit-risk-analysis
# Credit Risk Analysis with SQL and Python
- [English Version](#english-version)
- [Русская версия](#russian-version)

<a id="english-version"></a>
## English Version
A credit risk analysis project showcasing PD/LGD/ECL calculations on simulated data using PostgreSQL and Python.

### 📌 Table of Contents
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Database Setup](#-database-setup)
- [Running the Project](#-running-the-project)
- [Project Structure](#-project-structure)
- [SQL Query Examples](#-sql-query-examples)
- [Author](#-author)
- [Back to top](#credit-risk-analysis)


## 🛠 Requirements
- Python 3.7+
- PostgreSQL 12+
- Libraries:
  ```bash
  pip install psycopg2-binary pandas numpy

<a id="russian-version"></a>
## Русская версия
Проект демонстрирует анализ кредитного портфеля (расчет PD, LGD, ECL) на синтетических данных с использованием PostgreSQL и Python.

### 📌 Содержание
- [Требования](#-требования)
- [Установка](#-установка)
- [Настройка БД](#-настройка-базы-данных)
- [Запуск](#-запуск)
- [Структура проекта](#-структура-проекта)
- [Примеры SQL-запросов](#-примеры-sql-запросов)
- [Автор](#-автор)
- [Наверх](#credit-risk-analysis)

## 🛠 Требования
- Python 3.7+
- PostgreSQL 12+
- Библиотеки:
  ```bash
  pip install psycopg2-binary pandas numpy


## 🔧 Установка
Клонируйте репозиторий:

```bash
git clone https://github.com/ваш-логин/credit-risk-analysis.git
cd credit-risk-analysis
```

Установите зависимости:

```bash
pip install -r requirements.txt  # Если используете requirements.txt
```

## 🗄 Настройка базы данных

Создайте БД в PostgreSQL:

```sql
CREATE DATABASE credit_risk;
```

Создайте таблицы:

```sql
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS customers;
CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    customer_id INT,
    loan_amount NUMERIC,
    loan_type VARCHAR(20),
    interest_rate NUMERIC,
    term INT,
	issue_date DATE,
    status VARCHAR(20),
	credit_score_band VARCHAR(20),
	exposure_at_default NUMERIC(20,10),
    recovered_amount NUMERIC(20,10)
);
  

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    income NUMERIC,
    employment_length INT,
    region VARCHAR(50)
);
```
## 🚀 Запуск

Сгенерируйте тестовые данные:

```bash
python generate_data.py
```
Файлы loans.csv и customers.csv появятся в папке data/.

Импортируйте данные в PostgreSQL:

```bash
python import_data.py
```
Для выполнения SQL-запросов используйте:

```bash
psql -U ваш_пользователь -d credit_risk -f queries/1_pd_calculation.sql
```
