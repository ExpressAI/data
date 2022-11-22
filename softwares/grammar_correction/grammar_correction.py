from __future__ import annotations

from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware
from promptware.tasks import TaskType

grammar_correction = PromptConfig(
    name="grammar_correction",
    description="Corrects sentences into standard English.",
    instruction="Correct this to standard English:",
    demonstration=[],
    prompt_template=lambda input: f"{input['text']}\n",
    task=TaskType.conditional_generation,
)


class GrammarCorrectionPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="Corrects sentences into standard English.",
            creator="OpenAI",
            homepage="https://beta.openai.com/examples/default-grammar",
            reference="",
            codebase_url="https://beta.openai.com/examples/default-grammar",
            license=LicenseType.no_license,
            task=TaskType.conditional_generation,
        )

    def _kernel_configs(self):
        return {
            "openai": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=60,
                temperature=0,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            ),
        }

    def _software_configs(self):
        return {"grammar_correction": grammar_correction}
