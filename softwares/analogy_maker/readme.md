# Software: `softwares/analogy_maker`

This promptware is used to create analogies. Modified from a community prompt to require fewer examples.

```python
import promptware
software = promptware.install("analogy_maker")
output = software.execute("Questions are arrows in that:")
# output:
# Questions are like arrows in that they both have the potential to hit their target. Just as an arrow needs to be aimed correctly to hit its mark, a question needs to be asked in the right way to get the desired response.
```