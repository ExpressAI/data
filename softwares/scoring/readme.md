# Software: `scoring`

Given a text, it can generate the average log probabilities.

```python
import promptware
software = promptware.install("scoring")
output = software.execute("I love this movie")
# -3.8613948799999998
```