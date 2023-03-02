# Software: `softwares/extract_contact_information`

This promptware is used to extract contact information from a block of text.

```python
import promptware
software = promptware.install("extract_contact_information")
output = software.execute("Dear Kelly,\n\nIt was great to talk to you at the seminar. I thought Jane's talk was quite good.\n\nThank you for the book. Here's my address 2111 Ash Lane, Crestview CA 92002\n\nBest,\n\nMaya\n\nName:")
# output:
# Maya
# Mailing Address:
# 2111 Ash Lane, Crestview CA 92002
```