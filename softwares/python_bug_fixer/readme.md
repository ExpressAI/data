# Software: `softwares/python_bug_fixer`

This promptware is used to structure the prompt for checking for bugs. Here we add a comment suggesting that source code is buggy, and then ask codex to generate a fixed code.

```python
import promptware
software = promptware.install("python_bug_fixer")
output = software.execute("### Buggy Python\nimport Random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = "What is "+a+" x "+b+"? "\n    answer = input(question)\n    if answer = a*b\n        print (Well done!)\n    else:\n        print("No.")\n    \n### Fixed Python")
# output:
# import random
# a = random.randint(1,12)
# b = random.randint(1,12)
# for i in range(10):
#     question = "What is "+str(a)+" x "+str(b)+"? "
#     answer = int(input(question))
#     if answer == a*b:
#         print ("Well done!")
#     else:
#         print("No.")
```