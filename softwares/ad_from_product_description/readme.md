# Software: `softwares/ad_from_product_description`

This promptware is used to turn a product description into ad copy.

```python
import promptware
software = promptware.install("ad_from_product_description")
output = software.execute("Product: Learning Room is a virtual environment to help students from kindergarten to high school excel in school.")
# output:
# Learning Room is the perfect virtual environment for parents to help their children excel in school. With Learning Room, parents can help their children learn at their own pace, in a safe and secure environment.
```