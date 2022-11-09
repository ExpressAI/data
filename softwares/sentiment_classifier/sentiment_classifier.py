from __future__ import annotations

from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.promptware import PromptConfig, Promptware
from promptware.tasks import TaskType


class SentimentClassifierPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="This promptware is used to identify the sentiment of a "
            "sentence (positive or negative) based on some learning",
            homepage="",
            reference="",
            license="",
            codebase_url="",
        )

    def _kernel_configs(self):
        return {
            "openai": PLMKernelConfig(
                platform="openai",
                max_tokens=64,
                temperature=0,
                model_name="text-curie-001",
            )
        }

    def _software_configs(self):
        return {
            "sentiment_classification": PromptConfig(
                name="sentiment_classification",
                description="This promptware is used to identify the sentiment of a"
                " sentence (positive or negative) based on some learning"
                " samples from the sst2 dataset.",
                instruction="Give a sentence, classify the sentiment of it"
                " using negative and positive labels",
                demonstration=[
                    "I love this movie.\npositive",
                    "This movie is too boring.\nnegative",
                ],
                prompt_template=lambda input: f"{input['text']}",
                task=[TaskType.text_classification],
            )
        }
