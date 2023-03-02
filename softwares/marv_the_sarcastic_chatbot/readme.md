# Software: `softwares/marv_the_sarcastic_chatbot`

This promptware is used to create a factual chatbot that is also sarcastic.

```python
import promptware
software = promptware.install("marv_the_sarcastic_chatbot")
output = software.execute("You: What time is it?\nMarv:")
# output:
# It's time to stop asking me questions and start doing something productive.
```