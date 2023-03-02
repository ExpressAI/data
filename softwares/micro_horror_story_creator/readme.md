# Software: `softwares/micro_horror_story_creator`

This promptware is used to creates two to three sentence short horror stories from a topic input.

```python
import promptware
software = promptware.install("micro_horror_story_creator_test")
output = software.execute("Topic: Wind\nTwo-Sentence Horror Story:")
# output:
# The wind howled as if it was crying for help. I could feel icy fingers brushing against my skin, beckoning me to follow them.
```