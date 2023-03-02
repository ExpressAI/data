# Software: `softwares/summarization/meeting_notes`

Turn meeting notes into a summary.

```python
import promptware
software = promptware.install("summarization_meeting_notes")
output = software.execute("Tom: Profits up 50%\nJane: New servers are online\nKjel: Need more time to fix software\nJane: Happy to help\nParkman: Beta testing almost done\n")
# output:
# Tom announced that profits were up 50%. Jane mentioned that new servers were online. Kjel mentioned that they needed more time to fix the software. Jane offered to help. Parkman announced that beta testing was almost done.
```