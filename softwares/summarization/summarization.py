from __future__ import annotations

from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware
from promptware.tasks import TaskType

summarization_general = PromptConfig(
    name="summarization_general",
    description="Translates difficult text into simpler concepts.",
    instruction="Summarize the following text into simpler concepts:",
    demonstration=[],
    prompt_template=lambda input: f"{input['text']}\n",
    task=TaskType.summarization,
)

summarization_meeting_notes = PromptConfig(
    name="summarization_meeting_notes",
    description="Turn meeting notes into a summary.",
    instruction="Convert my short hand into a first-hand account of the meeting: ",
    demonstration=[],
    prompt_template=lambda input: f"{input['meeting_notes']}\n",
    task=TaskType.summarization,
)


class SummarizationPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="Summarize long text to short text.",
            creator="OpenAI",
            homepage="https://beta.openai.com/examples/",
            reference="",
            codebase_url="https://beta.openai.com/examples/",
            license=LicenseType.no_license,
            task=TaskType.qa_open_domain,
        )

    def _kernel_configs(self):
        return {
            "openai1": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=200,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            ),
            "openai2": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=100,
                temperature=0,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            ),
        }

    def execute(self, input):
        openai_kernel1 = self.kernel_configs["openai1"].to_kernel()
        openai_kernel2 = self.kernel_configs["openai2"].to_kernel()
        if self.config_name == "default" or self.config_name == "general":
            return self.normalize_output(
                openai_kernel1.execute(
                    input, self.software_configs["summarization_general"]
                )["text"]
            )
        if self.config_name == "meeting_notes":
            return self.normalize_output(
                openai_kernel2.execute(
                    input, self.software_configs["summarization_meeting_notes"]
                )["text"]
            )
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")

    def _software_configs(self):
        if self.config_name == "default" or self.config_name == "text":
            return {"summarization_general": summarization_general}
        elif self.config_name == "meeting_notes":
            return {"summarization_meeting_notes": summarization_meeting_notes}
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")
