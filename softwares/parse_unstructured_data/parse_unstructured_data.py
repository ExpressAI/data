from __future__ import annotations

from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware
from promptware.tasks import TaskType

parse_unstructured_data = PromptConfig(
    name="parse_unstructured_data",
    description="Create tables from long form text by specifying "
    "a structure and supplying some examples.",
    instruction="A table summarizing the following text.",
    demonstration=[],
    prompt_template=lambda input: f"{input['text']}\n{input['head']}\n",
    task=TaskType.conditional_generation,
)


class ParseUnstructuredDataPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="Answer questions based on existing knowledge.",
            creator="OpenAI",
            homepage="https://beta.openai.com/examples/default-parse-data",
            reference="",
            codebase_url="https://beta.openai.com/examples/default-parse-data",
            license=LicenseType.no_license,
            task=TaskType.conditional_generation,
        )

    def _kernel_configs(self):
        return {
            "openai": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=100,
                temperature=0,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            ),
        }

    def _software_configs(self):
        return {"parse_unstructured_data": parse_unstructured_data}
