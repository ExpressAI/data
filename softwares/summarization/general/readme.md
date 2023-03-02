# Software: `softwares/summarization/general`

Translates difficult text into simpler concepts.

```python
import promptware
software = promptware.install("summarization_general")
output = software.execute("Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.")
# output:
# Jupiter is a gas giant planet located fifth from the Sun, and is the largest planet in the solar system. It has a mass one thousandth that of the sun and is two and a half times that of all the other planets in the solar system combined. Jupiter is one of the brightest objects visible in the night sky, and has been known to ancient civilizations for centuries. It is named after the Roman god Jupiter. When viewed from Earth, it can cast shadows with its reflected light.
```