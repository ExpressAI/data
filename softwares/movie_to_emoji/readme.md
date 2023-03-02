# Software: `softwares/movie_to_emoji`

This promptware is used to convert movie titles into emoji.

```python
import promptware
software = promptware.install("movie_to_emoji")
output = software.execute("Star Wars:")
# output:
# ⭐️🌌
```