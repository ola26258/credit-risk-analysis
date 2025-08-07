### Задание 1: Определите долю дефолтных кредитов (status = 'default') от общего количества выданных кредитов в разрезе категорий кредитного скоринга (credit_score_band).
```sql
SELECT 
	credit_score_band, 
	ROUND(COUNT(CASE WHEN status='default' 
		THEN 1 
		ELSE NULL 
		END)*100.0/COUNT(*),2) AS PD
FROM loans
GROUP BY credit_score_band
```
<img width="274" height="142" alt="{9966ECF8-DDCB-4EEF-9EC9-DBDBEB54136F}" src="https://github.com/user-attachments/assets/964bbf7b-84a4-4b5b-9ae1-b6800cb4127e" />

### Задание 2: Рассчитайте ожидаемые потери для каждого типа кредита (loan_type).
```sql
WITH loan_metrics AS (
    SELECT 
        loan_type,
        ROUND(COUNT(CASE WHEN status='default' THEN 1 END) * 100.0 / COUNT(*), 2) AS pd_percent,
        ROUND(AVG(CASE WHEN status='default' THEN 1 - recovered_amount/NULLIF(exposure_at_default, 0) END), 2) AS lgd,
        ROUND(AVG(exposure_at_default), 2) AS ead
    FROM loans
    GROUP BY loan_type
)
SELECT 
    loan_type,
    pd_percent,
    lgd,
    ead,
    ROUND((pd_percent/100) * lgd * ead, 2) AS expected_loss
FROM loan_metrics
ORDER BY expected_loss DESC;
```
<img width="572" height="151" alt="{48C96CAC-464B-4DD3-81FD-7A942B1658D1}" src="https://github.com/user-attachments/assets/8f1fd1ec-33bf-45f4-ae6b-c5e36eb9e127" />

### Задание 3: Определите средний процент невозврата по регионам (region).
```sql
SELECT region,ROUND(AVG(1-recovered_amount/exposure_at_default),2) AS avg_LGD, COUNT(*) AS default_count
FROM loans RIGHT JOIN customers USING(customer_id)
WHERE status='default'
GROUP BY region
ORDER BY avg_lgd DESC;
```

<img width="379" height="168" alt="{6585BB46-697C-4109-97B7-AFDEA2414234}" src="https://github.com/user-attachments/assets/f13d28a4-cb75-4029-8144-a19088edf53b" />

### Задание 4: Разделите клиентов на 3 группы по доходу (income): низкий, средний, высокий — и сравните уровень дефолтов в каждой группе.
```sql
WITH income_groups AS
(SELECT customer_id, income, status, NTILE(3) OVER(ORDER BY income) AS income_group
FROM customers JOIN loans USING(customer_id))
SELECT 
  CASE 
    WHEN income_group = 1 THEN 'Низкий доход'
    WHEN income_group = 2 THEN 'Средний доход'
    WHEN income_group = 3 THEN 'Высокий доход'
  END AS income_category,
  COUNT(customer_id) AS total_clients,
  SUM(CASE WHEN status = 'default' THEN 1 ELSE 0 END) AS default_clients,
  ROUND(SUM(CASE WHEN status = 'default' THEN 1 ELSE 0 END) * 100.0 / COUNT(customer_id), 2) AS default_rate_percent
FROM income_groups
GROUP BY income_group
ORDER BY income_group;
```
<img width="535" height="123" alt="{A413B2D5-59CA-4327-B89B-FB755540D388}" src="https://github.com/user-attachments/assets/a59a5ce0-2f47-46f0-97ec-3c0464c42457" />


## Результаты анализа
Искусственно сгенерированные данные демонстрируют равномерное распределение дефолтов:
- По доходу: 10.5-10.9% во всех группах
- По городам: аналогичные показатели

**Вывод**: 
В данном наборе данных не выявлено значимой корреляции между доходом/городом и вероятностью дефолта. 
Анализ выполнен для демонстрации техники работы с оконными функциями (NTILE) и методов расчета процентных соотношений.

*Примечание: В реальных данных рекомендуется проверить дополнительные факторы (кредитная история, возраст клиента и др.)*
