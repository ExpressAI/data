# Software: `softwares/scoring`

Given a text, generate the average of its log probabilities

```python
import promptware
software = promptware.install("scoring")
output = software.execute("I love this movie")
# output:
# -
# 3
# .
# 8
# 6
# 1
# 3
# 9
# 4
# 8
# 7
# 9
# 9
# 9
# 9
# 9
# 9
# 9
# 8
```