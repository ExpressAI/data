# Software: `softwares/product_name_generator`

This promptware is used to create product names from examples words.

```python
import promptware
software = promptware.install("product_name_generator")
output = software.execute("Product description: A pair of shoes that can fit any foot size.\nSeed words: adaptable, fit, omni-fit.")
# output:
# Product names: AdaptFits, OmniShoes, FitAlls, FootFits.
```