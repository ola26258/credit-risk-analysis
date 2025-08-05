### Задание: Определите долю дефолтных кредитов (status = 'default') от общего количества выданных кредитов в разрезе категорий кредитного скоринга (credit_score_band).
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

### Задание: Рассчитайте ожидаемые потери для каждого типа кредита (loan_type)
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

#### LGD is really high. Check the data:

```sql
SELECT
    AVG(recovered_amount / NULLIF(exposure_at_default, 0)) * 100 AS avg_recovery_rate_percent,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY (recovered_amount / NULLIF(exposure_at_default, 0))) * 100 AS median_recovery_rate_percent
FROM loans
WHERE status = 'default' AND exposure_at_default > 0;
```
<img width="429" height="70" alt="{987C9F0A-88BA-4C40-9289-11FA05E49EAF}" src="https://github.com/user-attachments/assets/428b99b3-c238-4f88-b203-d8f19e75b2e2" />

