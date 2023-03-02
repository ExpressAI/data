# Software: `softwares/javascript_helper_chatbot`

This promptware is used to create a message-style chatbot that can answer questions about using JavaScript. It uses a few examples to get the conversation started.

```python
import promptware
software = promptware.install("javascript_helper_chatbot")
output = software.execute("You: How do you make an alert appear after 10 seconds?\nJavaScript chatbot")
# output:
# You can use the setTimeout() method.
```