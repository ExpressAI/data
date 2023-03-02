# Software: `softwares/natural_language_to_openai_api`

This promptware is used to convert natural lanugage to OpenAI API.

```python
import promptware
software = promptware.install("natural_language_to_openai_api")
output = software.execute(""""\nimport util\n"""\nCreate an OpenAI completion starting from the prompt "Once upon an AI", no more than 5 tokens. Does not include the prompt.\n"""\n")
# output:
# def completion_example():
#     openai = util.openai()
#     completion = openai.Completion.create(
#         prompt="Once upon an AI",
#         max_tokens=5,
#         temperature=1.0,
#         echo=False,
#     )
```