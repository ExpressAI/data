# Software: `softwares/sql_request`

This promptware is used to create simple SQL queries.

```python
import promptware
software = promptware.install("sql_request")
output = software.execute("Create a SQL request to find all users who live in California and have over 1000 credits:")
# output:
# SELECT * FROM users
# WHERE state = 'California'
# AND credits > 1000;
```