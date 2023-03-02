# Software: `softwares/text_to_command`

This promptware is used to convert the text to a programmatic command.

```python
import promptware
software = promptware.install("text_to_command")
output = software.execute("Reach out to the ski store and figure out if I can get my skis fixed before I leave on Thursday\n")
# output:
# send-msg `find ski store` Can you tell me if you have any skis in stock that I can use before I leave on Thursday?
```