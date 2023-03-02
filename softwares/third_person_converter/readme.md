# Software: `softwares/third_person_converter`

This promptware is used to converts first-person POV to the third-person. This is modified from a community prompt to use fewer examples.

```python
import promptware
software = promptware.install("third_person_converter")
output = software.execute("I decided to make a movie about Ada Lovelace.")
# output:
# She decided to make a movie about Ada Lovelace.
```