# Software: `softwares/sql_translate`

This promptware is used to translate natural language to SQL queries.

```python
import promptware
software = promptware.install("sql_translate")
output = software.execute("A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT")
# output:
# d.name
# FROM
#     Department d
#     INNER JOIN Employee e ON d.id = e.department_id
#     INNER JOIN Salary_Payments sp ON e.id = sp.employee_id
# WHERE
#     sp.date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
# GROUP BY
#     d.name
# HAVING
#     COUNT(e.id) > 10
```