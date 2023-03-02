# Software: `softwares/javascript_one_line_function`

This promptware is used to turn a JavaScript function into a one liner.

```python
import promptware
software = promptware.install("javascript_one_line_function")
output = software.execute("dogs.forEach((dog) => {\n    car.push(dog);\n});\n\nJavaScript one line version:")
# output:
# dogs.forEach((dog) => car.push(dog))
```