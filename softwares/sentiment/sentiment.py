from explainaboard.constants import TaskType
from promptware.promptware import PromptConfig

sentiment_classification = PromptConfig(
    name="sentiment_classification",
    description="This promptware is used to identify the sentiment of a"
    " sentence (positive or negative) based on some learning"
    " samples from the sst2 dataset.",
    instruction="Give a sentence, classify the sentiment of it using negative"
    " and positive labels",
    demonstration=[
        "I love this movie.\npositive",
        "This movie is too boring.\nnegative",
    ],
    prompt_template=lambda input: f"{input['text']}",
    task=[
        TaskType.text_classification.value,
    ],
)
