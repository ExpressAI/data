# Software: `softwares/gaokao_grammar_correction`

Gaokao English Grammar Correction

```python
import promptware
software = promptware.install("gaokao_grammar_correction")
output = software.execute("During my last winter holiday, I went to countryside with my father to visit my grandparents. I find a big change there. The first time I went there, they were living in a small house with dogs, ducks, and another animals. Last winter when I went here again, they had a big separate house to raise dozens of chicken. They also had a small pond which they raised fish. My grandpa said last summer they earned quite a lot by sell the fish. I felt happily that their life had improved. At the end of our trip, I told my father that I planned to return for every two years, but he agreed.")
# output:
# During my last winter holiday, I went to the countryside with my father to visit my grandparents. I found a big change there. The first time I went there, they were living in a small house with dogs, ducks, and other animals. Last winter when I went there again, they had a big separate house to raise dozens of chickens. They also had a small pond which they raised fish in. My grandpa said that last summer they earned quite a lot by selling the fish. I felt happily that their life had improved. At the end of our trip, I told my father that I planned to return every two years, but he agreed.
```