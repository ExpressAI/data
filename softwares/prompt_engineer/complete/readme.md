# Software: `prompt_engineer`


## Example

### Code
```python
import promptware
software = promptware.install("prompt_engineer")
input = [
    ("aperiodic", "periodic"),
    ("unsent", "sent"),
]
output = software.execute(input)
output = {"text":"the antonym of the word.", "score":-0.166}

```

### Complete prompt of this example
```text
 GPT3 is a good prompt engineer and it can help us to generate instruction based on input and output pairs.
 
 I gave a friend an instruction. Based on the instruction they produced the following input-output pairs:
 
 Input: I love this movie.
 Output: positive
 
 Input: The movie is boring.
 Output: negative
 
 The instruction was to  find: the sentiment of the movie review.
 
 I gave a friend an instruction. Based on the instruction they produced the following input-output pairs:
 
 Input:aperiodic
 Output:periodic
 
 Input:unsent
 Output:sent
 
 The instruction was to  find:
```



```python

import promptware
software = promptware.install("./softwares/prompt_engineer", "insert")
input = [
    ("aperiodic", "periodic"),
    ("unsent", "sent"),
    ("sad","happy"),
]
output = software.execute(input)
print(output)

#{'text': 'find the antonym of the word', 'score': -0.150508175}
```


### Complete prompt of this example
```text
GPT3 is a good prompt engineer and it can help us to generate instruction based on input and output pairs.

I instructed my friend to find the sentiment of the movie review. The friend read the instruction and wrote an output for every one of the inputs. Here are the input-output pairs:

Input: I love this movie.
Output: positive

Input: The movie is boring.
Output: negative

Input: I love this book.
Output: positive

I instructed my friend to [INSERT]. The friend read the instruction and wrote an output for every one of the inputs. Here are the input-output pairs:

Input:aperiodic
Output:periodic

Input:unsent
Output:sent

Input:sad
Output:happy

```
