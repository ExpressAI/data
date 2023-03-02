# Software: `softwares/write_a_python_docstring`

This promptware is used to create a docstring for a given Python function. We specify the Python version, paste in the code, and then ask within a comment for a docstring, and give a characteristic beginning of a docstring (""").

```python
import promptware
software = promptware.install("write_a_python_docstring")
output = software.execute("# Python 3.7\n \ndef randomly_split_dataset(folder, filename, split_ratio=[0.8, 0.2]):\n    df = pd.read_json(folder + filename, lines=True)\n    train_name, test_name = "train.jsonl", "test.jsonl"\n    df_train, df_test = train_test_split(df, test_size=split_ratio[1], random_state=42)\n    df_train.to_json(folder + train_name, orient='records', lines=True)\n    df_test.to_json(folder + test_name, orient='records', lines=True)\nrandomly_split_dataset('finetune_data/', 'dataset.jsonl')\n    \n# An elaborate, high quality docstring for the above function:\n"""")
# output:
# This function randomly splits a dataset into two parts, a training set and a test set, and saves them as separate files.
# 
# Parameters:
#     folder (str): The path to the folder containing the dataset file.
#     filename (str): The name of the dataset file.
#     split_ratio (list): A list of two floats representing the ratio of the training set and the test set.
# 
# Returns:
#     None
```