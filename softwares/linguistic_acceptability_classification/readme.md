# Software: `softwares/linguistic_acceptability_classification`

This promptware is used to identify whether a sentence is a grammatical English sentence based on some learning samples from the cola dataset.

```python
import promptware
software = promptware.install("linguistic_acceptability_classification")
output = software.execute("Bill pushed Harry off the sofa.")
# output:
# yes
```