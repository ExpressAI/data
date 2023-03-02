# Software: `softwares/sentiment_classifier`

This promptware is used to identify the sentiment of a sentence (positive or negative) based on some learning samples from the sst2 dataset.

```python
import promptware
software = promptware.install("sentiment_classification")
output = software.execute("I love this movie.")
# output:
# positive
```