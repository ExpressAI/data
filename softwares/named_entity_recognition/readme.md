# Software: `softwares/named_entity_recognition`

This promptware is used to extract entities in the text

```python
import promptware
software = promptware.install("named-entity-recognition")
output = software.execute("I will go to New York on Saturday.")
# output:
# New York.
```