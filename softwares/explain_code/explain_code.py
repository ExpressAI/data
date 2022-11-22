from __future__ import annotations

from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware
from promptware.tasks import TaskType

explain_code_general = PromptConfig(
    name="explain_code_general",
    description="Explain a complicated piece of code.",
    instruction="A table summarizing the following text.",
    demonstration=[],
    prompt_template=lambda input: f"{input['code']}\n\"\"\"\n"
    "Here's what the above code is doing:\n1.",
    task=TaskType.conditional_generation,
)

explain_code_python = PromptConfig(
    name="explain_code_python",
    description="Explain a piece of Python code in human understandable language.",
    instruction="A table summarizing the following text.",
    demonstration=[],
    prompt_template=lambda input: f"{input['code']}\n# Explanation of"
    " what the code does\n#",
    task=TaskType.conditional_generation,
)


class ExplainCodePromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="Explain a complicated piece of code.",
            creator="OpenAI",
            homepage="https://beta.openai.com/examples/default-explain-code",
            reference="",
            codebase_url="https://beta.openai.com/examples/default-explain-code",
            license=LicenseType.no_license,
            task=TaskType.conditional_generation,
        )

    def _kernel_configs(self):
        return {
            "openai1": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=64,
                temperature=0,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            ),
            "openai2": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=64,
                temperature=0,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            ),
        }

    def execute(self, input):
        openai_kernel1 = self.kernel_configs["openai1"].to_kernel()
        openai_kernel2 = self.kernel_configs["openai2"].to_kernel()
        if self.config_name == "default" or self.config_name == "text":
            return self.normalize_output(
                openai_kernel1.execute(
                    input, self.software_configs["explain_code_general"]
                )["text"]
            )
        elif self.config_name == "python":
            return self.normalize_output(
                openai_kernel2.execute(
                    input, self.software_configs["explain_code_python"]
                )["text"]
            )
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")

    def _software_configs(self):
        if self.config_name == "default" or self.config_name == "general":
            return {"explain_code_general": explain_code_general}
        elif self.config_name == "python":
            return {"explain_code_python": explain_code_python}
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")
