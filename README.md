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


## 🛠 Requirements
- Python 3.7+
- PostgreSQL 12+
- Libraries:
  ```bash
  pip install psycopg2-binary pandas numpy

  ## 🔧 Installation
Clone the repository:

```bash
git clone https://github.com/ваш-логин/credit-risk-analysis.git
cd credit-risk-analysis
```

Install the dependencies:

```bash
pip install -r requirements.txt  # If you use requirements.txt
```

## 🗄 Database Setup

Create database in PostgreSQL:

```sql
CREATE DATABASE credit_risk;
```

Create tables:

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
## 🚀 Running the project

Generate data:

```bash
python generate_data.py
```
After running the script, loans.csv and customers.csv will appear in the data/ directory.

Import data into PostgreSQL:

```bash
python import_data.py
```
Run SQL script:

```bash
psql -U your_username -d credit_risk -f queries/1_pd_calculation.sql
```

## 📂 Project Structure

credit-risk-analysis/ \
├── data/                                      # CSV-files containing raw data \
│   ├── loans.csv                              # Loan portfolio data (amounts, types, statuses, risk metrics) \
│   └── customers.csv                          # Customer demographics and financial profiles \
├── docs/                                      # Documentation files \
│   └── ER_diagram.png                         # Entity-Relationship diagram of database schema \
├── generate_data.py                           # Python script to generate synthetic loan data \
├── import_data.py                             # Data loader for database population \
├── README.md                                  # Main project documentation (this file) \
└── Questions_and_Answers.md                   # Common analytical scenarios with solutions

<a id="russian-version"></a>
## Русская версия
Проект демонстрирует анализ кредитного портфеля (расчет PD, LGD, ECL) на синтетических данных с использованием PostgreSQL и Python.

### 📌 Содержание
- [Требования](#-требования)
- [Установка](#-установка)
- [Настройка БД](#-настройка-базы-данных)
- [Запуск](#-запуск)
- [Структура проекта](#-структура-проекта)
  
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
## 📂 Структура проекта

credit-risk-analysis/ \
├── data/                  	 # CSV-файлы с данными \
│   ├── loans.csv \
│   └── customers.csv \
├── docs/                 	 # Документация \
│   └── ER_diagram.png \
├── generate_data.py      	 # Генератор тестовых данных \
├── import_data.py        	 # Импорт в PostgreSQL \
├── README.md              	 # Этот файл \
└── Questions _and_Answers.md	 # Примеры заданий
