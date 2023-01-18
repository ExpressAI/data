from __future__ import annotations

from promptware.constants import (
    ApplicationCategory,
    ApplicationSubcategory,
    DesignPatternType,
    LanguageType,
    LicenseType,
    PlatformType,
    TaskType,
)
from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.promptware import PromptConfig, Promptware

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
            research_tasks=[TaskType.conditional_generation],
            application_categories=[ApplicationCategory.transformation],
            application_subcategories=[ApplicationSubcategory.explanation],
            original_platform=PlatformType.gpt3,
            design_pattern=DesignPatternType.standalone,
            source_language=LanguageType.python,
            target_language=LanguageType.en,
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
            code = self.get_code(input, self.software_configs["explain_code_general"])
            return self.normalize_output(openai_kernel1.execute(code)["text"])
        elif self.config_name == "python":
            code = self.get_code(input, self.software_configs["explain_code_python"])
            return self.normalize_output(openai_kernel2.execute(code)["text"])
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")

    def _software_configs(self):
        if self.config_name == "default" or self.config_name == "general":
            return {"explain_code_general": explain_code_general}
        elif self.config_name == "python":
            return {"explain_code_python": explain_code_python}
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")

    def _example(self):
        code_block = """class Log:
                def __init__(self, path):
                    dirname = os.path.dirname(path)
                    os.makedirs(dirname, exist_ok=True)
                    f = open(path, "a+")
                    # Check that the file is newline-terminated
                    size = os.path.getsize(path)
                    if size > 0:
                        f.seek(size - 1)
                        end = f.read(1)
                        if end != "\n":
                            f.write("\n")
                    self.f = f
                    self.path = path
                def log(self, event):
                    event["_event_id"] = str(uuid.uuid4())
                    json.dump(event, self.f)
                    self.f.write("\n")
                def state(self):
                    state = {"complete": set(), "last": None}
                    for line in open(self.path):
                        event = json.loads(line)
                        if event["type"] == "submit" and event["success"]:
                            state["complete"].add(event["id"])
                            state["last"] = event
                    return state"""
        if self.config_name == "default" or self.config_name == "general":
            return {
                "input": {"code": code_block},
                "output": "The class Log is defined, and its __init__() method"
                " is called.\n2.\nThe path to the file to be logged"
                " is determined.\n3.\nThe file is opened for writing."
                "\n4.\nEach line of the file is read and parsed into"
                " an event object.\n5.",
            }
        elif self.config_name == "python":
            return {
                "input": {"code": code_block},
                "output": "The code first creates a Log object, specifying the path"
                " to a file. If the file does not exist, the code creates"
                " the file and sets the path variable to the path.\n\nNext,"
                " the code checks to see if the file is newline-terminated."
                " If it is not, the code reads",
            }
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")
