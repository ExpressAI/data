# Software: `softwares/grammar_correction`

Corrects sentences into standard English.

```python
import promptware
software = promptware.install("grammar_correction")
output = software.execute("She no went to the market.")
# output:
# She didn't go to the market.
```