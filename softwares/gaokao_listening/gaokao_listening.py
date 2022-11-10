from __future__ import annotations

import re

from nltk import sent_tokenize

from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware
from promptware.tasks import TaskType


def truncate(text, num=512):
    """Keep text length around 512 by default"""
    text_tokens = text.split(" ")
    if len(text_tokens) <= num:
        return text
    total = 0
    sents = sent_tokenize(text)
    final_sents = []
    for i in range(len(sents)):
        if total < num:
            final_sents.append(sents[i])
            total += len(sents[i].split(" "))
        else:
            break
    return " ".join(final_sents)


def normalize_text(text):
    text = re.sub("\n+", " ", text)
    text = re.sub("\t", " ", text)
    text = re.sub(" +", " ", text)
    text = text.encode("ascii", "ignore").decode()
    text = text.strip()
    if len(text) == 0:
        return None
    return text


def preprocess_context(context):
    cont = context.replace("W:", "The woman said:").replace("M:", "The man said:")
    return truncate(normalize_text(cont), 600)


def preprocess_options(options: list[str]):
    options = [f'"{o}"' for o in options]
    return ", ".join(options[:-1]) + " or " + options[-1]


gaokao_listening = PromptConfig(
    name="gaokao_listening",
    description="Gaokao English Listening",
    instruction="",
    demonstration=[
        'The woman said: "Have you seen the movie "Hangover"? We went to see it'
        ' last night." The man said: "How was it?" The woman said: "Jason'
        ' thought it was extremely amusing, but I was a bit disappointed."\nWhat'
        ' does the woman think of the movie? "It\'s amusing.", "It\'s exciting." or'
        " \"It's disappointing.\"?\nIt's disappointing.\n",
        'The man said: "Susan, I heard you are going to France. How long will you'
        ' be staying there?" The woman said: "A whole year. My aunt lives there.'
        " I'm going to do a one-month course at a language school and spend the rest"
        ' of the time traveling."\nHow will Susan spend most of her time in'
        ' France? "Traveling around.", "Studying at a school." or "Looking'
        ' after her aunt."?\nTraveling around.\n',
    ],
    prompt_template=lambda input: f"{preprocess_context(input['context'])}\n"
    f"{input['question']} "
    f"{preprocess_options(input['options'])}?",
    task=TaskType.qa_multiple_choice,
)


class GaokaoListeningPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="gaokao_listening",
            creator="Promptware Authors",
            homepage="https://github.com/expressai/promptware",
            reference="",
            codebase_url="https://github.com/expressai/promptware/tree/main/softwares",
            license=LicenseType.apache_2_0,
            task=TaskType.qa_multiple_choice,
        )

    def _kernel_configs(self):
        return {
            "openai": PLMKernelConfig(
                platform="openai",
                model_name="text-davinci-002",
                max_tokens=20,
                temperature=0.0,
            )
        }

    def _software_configs(self):
        return {"gaokao_listening": gaokao_listening}
