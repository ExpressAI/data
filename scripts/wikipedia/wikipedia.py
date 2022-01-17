# coding=utf-8


"""Dataset config script for ag_news （this code is originally from huggingface, them modified by datalab）"""

import os
import csv
import sys
import importlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import Dict, List, Any, Optional, Iterator
import datalabs
from datalabs.tasks import TextClassification
from datalabs import StructuredTextData
from datalabs.operations.featurize.featurizing import featurizing, Featurizing
from .featurize import featurize as featurize


_DESCRIPTION = """\
AG is a collection of more than 1 million news articles. News articles have been
gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of
activity. ComeToMyHead is an academic news search engine which has been running
since July, 2004. The dataset is provided by the academic comunity for research
purposes in data mining (clustering, classification, etc), information retrieval
(ranking, search, etc), xml, data compression, data streaming, and any other
non-commercial activity. For more information, please refer to the link
http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .

The AG's news topic classification dataset is constructed by Xiang Zhang
(xiang.zhang@nyu.edu) from the dataset above. It is used as a text
classification benchmark in the following paper: Xiang Zhang, Junbo Zhao, Yann
LeCun. Character-level Convolutional Networks for Text Classification. Advances
in Neural Information Processing Systems 28 (NIPS 2015).
"""

_CITATION = """\
@inproceedings{Zhang2015CharacterlevelCN,
  title={Character-level Convolutional Networks for Text Classification},
  author={Xiang Zhang and Junbo Jake Zhao and Yann LeCun},
  booktitle={NIPS},
  year={2015}
}
"""

_TRAIN_DOWNLOAD_URL = "https://raw.githubusercontent.com/mhjabreel/CharCnn_Keras/master/data/ag_news_csv/train.csv"
_TEST_DOWNLOAD_URL = "https://raw.githubusercontent.com/mhjabreel/CharCnn_Keras/master/data/ag_news_csv/test.csv"



def get_operations(module_path:str):
    all_operations = {}
    #module = importlib.import_module(module_path)
    module = featurize

    target_class = None
    # print(module)
    for name, obj in module.__dict__.items():
        if isinstance(obj, type) and issubclass(obj, Featurizing):
            #and "_data_type" in obj.__dict__.items():
            # print(obj.__dict__.items())
            target_class = obj
            break


    if target_class == None:
        raise ValueError("target class is none!")

    for name, obj in module.__dict__.items():
        if isinstance(obj, target_class):
            all_operations[obj] = name

    return all_operations


# class AGNewsDataset(Dataset):
#     def apply(self, func):
#         if func._type == 'Aggregating':


class Wikipedia(StructuredTextData):


    def __init__(self, data:Iterator = None):

        self.data = [{"text":"This is a good movie"}]
        self.homedir = os.environ['HOME']
        self.data_remote = "https://dumps.wikimedia.org/other/static_html_dumps/current/en/wikipedia-en-html.tar.7z"
        self.max_cpu = os.cpu_count()
        self.data_local = self.download_to_local()


    def __repr__(self):

        module_path = "featurize"
        all_operations = get_operations(module_path)
        # print(all_operations)

        repr = "\n\t" + "data_local_directory: " + self.data_local + "\n\t"
        repr += f"Following operations can be applied: \n\t"
        repr += "\n\t\t - ".join([v for k, v in all_operations.items()])
        repr += "\n\t\n\t" + f"Example: data.apply({list(all_operations.values())[0]}))"
        # repr = "\n".join([f"{k}: {v}" for k, v in self.items()])
        # repr = re.sub(r"^", " " * 4, repr, 0, re.M)
        return f"StructureTextData({{\n{repr}\n}})"



    def download_to_local(self):
        homedir = self.homedir
        os.makedirs(f"{homedir}/.cache", exist_ok=True)
        if not os.path.exists(f"{homedir}/.cache/wikipedia/en"):
            os.makedirs(f"{homedir}/.cache/wikipedia", exist_ok=True)
            os.makedirs(f"{homedir}/.cache/wikipedia/en")
            # Download and extract data
            # TODO: Use python package instead of 7z. pip install py7zr
            os.system(f"wget {self.data_remote} -O {homedir}/.cache/wikipedia-en-html.tar.7z")
            os.system(f"7z x -so {homedir}/.cache/wikipedia-en-html.tar.7z | tar xf - -C {homedir}/.cache/wikipedia")
        return f"{homedir}/.cache/wikipedia/en"



    def apply(self, func):
        for sample in self.data:
            yield func(sample)
