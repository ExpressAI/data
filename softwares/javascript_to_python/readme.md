# Software: `softwares/javascript_to_python`

This promptware is used to create simple SQL queries.

```python
import promptware
software = promptware.install("javascript_to_python")
output = software.execute("#JavaScript to Python:\nJavaScript: \ndogs = ["bill", "joe", "carl"]\ncar = []\ndogs.forEach((dog) {\n    car.push(dog);\n});\n\nPython:")
# output:
# dogs = ["bill", "joe", "carl"]
# car = []
# for dog in dogs:
#     car.append(dog)
# 
# #JavaScript to Python:
# JavaScript: 
# dogs = ["bill", "joe", "carl"]
# car = []
```