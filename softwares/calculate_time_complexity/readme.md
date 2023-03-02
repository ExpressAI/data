# Software: `softwares/calculate_time_complexity`

This promptware is used to find the time complexity of a function.

```python
import promptware
software = promptware.install("calculate_time_complexity")
output = software.execute("def foo(n, k):\naccum = 0\nfor i in range(n):\n    for l in range(k):\n        accum += i\nreturn accum\n"""\nThe time complexity of this function is")
# output:
# O(n*k).
```