# Software: `softwares/turn_by_turn_directions`

This promptware is used to convert natural language to turn-by-turn directions.

```python
import promptware
software = promptware.install("turn_by_turn_directions")
output = software.execute("Go south on 95 until you hit Sunrise boulevard then take it east to us 1 and head south. Tom Jenkins bbq will be on the left after several miles.")
# output:
# 1. Go south on 95
# 2. Take Sunrise Boulevard east
# 3. Head south on US 1
# 4. Tom Jenkins BBQ will be on the left after several miles
```