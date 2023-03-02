# Software: `softwares/create_study_notes`

This promptware is used to provide a topic and get study notes.

```python
import promptware
software = promptware.install("create_study_notes")
output = software.execute("What are 5 key points I should know when studying Ancient Rome?")
# output:
# 1. The Roman Republic: This was the period of Ancient Rome from 509 BC to 27 BC, when it was ruled by a senate and two consuls.
# 
# 2. The Roman Empire: This was the period of Ancient Rome from 27 BC to 476 AD, when it was ruled by an emperor.
# 
# 3. Roman Law: This was the system of laws that governed the Roman Republic and Empire. It was based on the Twelve Tables, a set of laws written in the 5th century BC.
# 
# 4. Roman Religion: This was the religion of Ancient Rome, which was polytheistic and focused on the worship of gods and goddesses.
# 
# 5. Roman Architecture: This was the style of architecture
```