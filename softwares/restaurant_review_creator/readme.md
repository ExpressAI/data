# Software: `softwares/restaurant_review_creator`

This promptware is used to turn a few words into a restaurant review.

```python
import promptware
software = promptware.install("restaurant_review_creator")
output = software.execute("Name: The Blue Wharf\nLobster great, noisy, service polite, prices good.\n\nReview:")
# output:
# I recently visited The Blue Wharf for dinner and had a great experience. The lobster was especially delicious - definitely the highlight of the meal. The only downside was that it was a bit noisy, but the polite service more than made up for it. Prices were also very reasonable, making it a great value overall.
```