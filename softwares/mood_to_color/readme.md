# Software: `softwares/mood_to_color`

This promptware is used to turn a text description into a color.

```python
import promptware
software = promptware.install("mood_to_color")
output = software.execute("The CSS code for a color like a blue sky at dusk:")
# output:
# 3A539B
```