# Software: `softwares/translate_programming_languages`

This promptware is used to translate from one programming language to another we can use the comments to specify the source and target languages.

```python
import promptware
software = promptware.install("translate_programming_languages")
output = software.execute("##### Translate this function from Python into Haskell\n### Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n    \n### Haskell")
# output:
# ```haskell
# predictProba :: [String] -> [Double]
# predictProba xs = map predictOneProbas xs
# ```
```