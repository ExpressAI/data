# Software: `softwares/conversation/sarcastic`

Marv is a factual chatbot that is also sarcastic.

```python
import promptware
software = promptware.install("conversation_sarcastic")
output = software.execute("I'd like to cancel my subscription.")
# output:
# You can cancel your subscription at any time by clicking on the link in the email we sent you. Thanks for using Marv!
```