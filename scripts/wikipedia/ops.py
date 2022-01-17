from typing import Dict, List, Any, Optional
from typing import Callable, Mapping
from datalabs.operations.featurize.featurizing import Featurizing, featurizing
from multiprocessing import Pool
import json
from lxml import etree

class WikipediaFeaturizing(Featurizing):


    def __init__(self, *args, **kwargs
                 ):

        super(WikipediaFeaturizing, self).__init__(*args, **kwargs)
        self._type = 'WikipediaFeaturizing'
        self._data_type = "wikipedia"



class wikipedia_featurizing(featurizing):
    def __init__(self, *args, **kwargs
                 ):


        super(wikipedia_featurizing, self).__init__(*args, **kwargs)
        # print(self.__dict__)


    def __call__(self, *param_arg):
        if callable(self.name):

            tf_class = WikipediaFeaturizing(name = self.name.__name__, func=self.name)
            return tf_class(*param_arg)
        else:
            f = param_arg[0]

            name = self.name or f.__name__
            tf_cls = WikipediaFeaturizing(name=name, func = f,
                                   resources = self.resources,
                                   contributor = self.contributor,
                                    task = self.task,
                                    description=self.description,
                                    processed_fields=self.processed_fields,
                                    )
            return tf_cls



"""
from datalabs import load_dataset
data = load_dataset('./wikipedia')
from wikipedia.featurize import *
 
res = data.apply(get_number_of_tokens)
print(next(res))
"""


def process_relations(filepath_):
    wiki_extractor = WikiExtractor()
    out_ = wiki_extractor.extract_relations(filepath_)
    return out_


def process_text_entities(filepath_):
    wiki_extractor = WikiExtractor()
    out_ = wiki_extractor.extract_text_entities(filepath_)
    return out_


def process_toc(filepath_):
    wiki_extractor = WikiExtractor()
    out_ = wiki_extractor.extract_toc(filepath_)
    return out_


class WikiExtractor:
    """ Extract information from Wikipedia webpage (HTML)
        Extracted information including:
        * Table of contents
            {
                "Creation": [
                    "Development": [],
                    "Design": []],
                    "Personality": [
                        "Childhood": []],
                        "Adulthood": []]
                    ]
                ]
            }
        * Relations
            [
                ('First appearance', 'Naruto chapter 3: Enter Sasuke! (1999)'),
                ('Created by', 'Masashi Kishimoto')
            ]
        * text
            {
                'Sasuke Uchiha':
                    [
                        {'text': '\n', 'entities': []},
                        {'text': '\n', 'entities': []},
                        {'text': 'Sasuke Uchiha (Japanese: うちは サスケ, Hepburn: Uchiha Sasuke) ...'
                        'entities':
                            [
                                'fictional character',
                                'manga',
                                ...
                            ]
                    ],
                'Creation': [],
                ...
            }
    """

    def get_iter_text(self, e):
        """ Iteratively get texts from an element. """
        txt = ""
        for x in e.itertext():
            txt += x
        return txt

    def read_data(self, filepath=None):
        if filepath is not None:
            with open(filepath, "r", errors='ignore') as f:
                data = f.read()

        str_html = etree.HTML(data)
        return str_html

    def extract_toc(self, filepath=None):
        try:
            str_html = self.read_data(filepath)
            toc = {}

            def extract_toc_text_from_li(li_):
                toc_ = {}
                curr_text_ = self.get_iter_text(li_.xpath("./a/span[@class='toctext']")[0])
                lis_ = li_.xpath("./ul/li")
                toc_[curr_text_] = []
                if len(lis_) != 0:
                    for li_ in lis_:
                        toc_[curr_text_].append(extract_toc_text_from_li(li_))
                return toc_

            lis = str_html.xpath("//div[@id='toc']/ul/li")
            for li in lis:
                toc.update(extract_toc_text_from_li(li))
            return toc
        except:
            return None

    def extract_relations(self, filepath=None):
        try:
            str_html = self.read_data(filepath)
            rel = []
            trs = str_html.xpath("//table[@class='infobox']/tbody/tr")
            for tr in trs:
                th = tr.xpath("./th[@class='infobox-label']")
                if len(th) > 0:
                    th_txt = self.get_iter_text(th[0]).replace("\n", "")
                    td = tr.xpath("./td[@class='infobox-data']")
                    td_txt = self.get_iter_text(td[0]).replace("\n", "")
                    rel.append((th_txt, td_txt))
            return rel
        except:
            return None

    def extract_text_entities(self, filepath=None):
        try:
            str_html = self.read_data(filepath)

            def get_entities_in_text(txt_):
                ents_ = []
                as_ = txt_.xpath(".//a")
                for a_ in as_:
                    ent_ = self.get_iter_text(a_)
                    if len(ent_) > 0:
                        ents_.append(self.get_iter_text(a_))
                return ents_

            text = {}
            ps_and_spans = str_html.xpath("//p | //span[@class='mw-headline']")

            if ps_and_spans[0].tag == "span":
                title = self.get_iter_text(ps_and_spans[0])
            else:
                title = self.name

            txt_list = []
            for x in ps_and_spans:
                if x.tag == "span":
                    text[title] = txt_list
                    txt_list = []
                    title = self.get_iter_text(x)
                else:
                    txt_with_ents = {"text": self.get_iter_text(x), "entities": get_entities_in_text(x)}
                    txt_list.append(txt_with_ents)
            text[title] = txt_list
            return text
        except:
            return None



@wikipedia_featurizing(name = "get_number_of_tokens", contributor= "datalab", processed_fields= "text",
                                 task="text-classification", description="this function is used to calculate the text length",
                                 )
def get_number_of_tokens(sample:dict):
    return len(sample['text'])



def process_all_files(self, outpath, process):
    file = open(outpath, "w")
    count = 0
    # path = f"{self.homedir}/.cache/wikipedia/en"
    path = "/data/pliu3/reST/code/sketch/en"
    for root, dirnames, filenames in os.walk(path):
        filepaths = [os.path.join(root, filename) for filename in filenames if filename.endswith("html")]
        count += len(filepaths)
        with Pool(self.max_cpu) as p:
            outs = p.map(process, filepaths)
        for out in outs:
            if out is not None:
                print(json.dumps(out), file=file)
        print(f"Dealt with {count} files.")
        file.flush()
    file.flush()


@wikipedia_featurizing(name = "extract_relations", contributor= "datalab", processed_fields= "text",
                                 task="unsupervised data", description="this function is used for ")
def extract_relations(outpath):
    process_all_files(outpath, process_relations)


@wikipedia_featurizing(name = "extract_text_entities", contributor= "datalab", processed_fields= "text",
                                 task="unsupervised data", description="this function is used for ")
def extract_text_entities(outpath):
    process_all_files(outpath, process_text_entities)


@wikipedia_featurizing(name = "extract_toc", contributor= "datalab", processed_fields= "text",
                                 task="unsupervised data", description="this function is used for ")
def extract_toc(outpath):
    process_all_files(outpath, process_toc)







