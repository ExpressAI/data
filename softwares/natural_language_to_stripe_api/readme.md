# Software: `softwares/natural_language_to_stripe_api`

This promptware is used to convert natural lanugage to Stripe API.

```python
import promptware
software = promptware.install("natural_language_to_stripe_api")
output = software.execute("import util\n"""\nCreate a Stripe token using the users credit card: 5555-4444-3333-2222, expiration date 12 / 28, cvc 521\n"""")
# output:
# token = stripe.Token.create(
#     card={
#         "number": "5555-4444-3333-2222",
#         "exp_month": 12,
#         "exp_year": 28,
#         "cvc": "521"
#     },
# )
```