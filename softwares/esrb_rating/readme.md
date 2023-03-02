# Software: `softwares/esrb_rating`

This promptware is used to categorize text based upon ESRB ratings.

```python
import promptware
software = promptware.install("esrb_rating")
output = software.execute(""i'm going to blow your brains out with my ray gun then stomp on your guts."\n\nESRB rating:")
# output:
# Mature (M)
```