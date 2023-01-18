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

conversation_general = PromptConfig(
    name="conversation_general",
    description="Open ended conversation with an AI assistant.",
    instruction="The following is a conversation with an AI assistant. "
    "The assistant is helpful, creative, clever, and very friendly.",
    demonstration=[
        "Human: Hello, who are you?\n"
        "AI: I am an AI created by OpenAI. How can I help you today?\n",
    ],
    prompt_template=lambda input: f"Human: {input['text']}\nAI:",
    task=TaskType.qa_open_domain,
)

conversation_friend = PromptConfig(
    name="conversation_friend",
    description="Emulate a text message conversation.",
    instruction="",
    demonstration=[
        "You: What have you been up to?\n"
        "Friend: Watching old movies.\n"
        "You: Did you watch anything interesting?\n"
        "Friend: Yes, I watched The Omen and Troy.",
    ],
    prompt_template=lambda input: f"You: {input['text']}\nFriend:",
    task=TaskType.qa_open_domain,
)

conversation_sarcastic = PromptConfig(
    name="conversation_sarcastic",
    description="Marv is a factual chatbot that is also sarcastic.",
    instruction="Marv is a chatbot that reluctantly "
    "answers questions with sarcastic responses:",
    demonstration=[
        "You: How many pounds are in a kilogram?\n"
        "Marv: This again? There are 2.2 pounds "
        "in a kilogram. Please make a note of this.\n"
        "You: What does HTML stand for?\n"
        "Marv: Was Google too busy? Hypertext Markup Language. "
        "The T is for try to ask better questions in the future.\n"
        "You: When did the first airplane fly?\n"
        "Marv: On December 17, 1903, Wilbur and Orville Wright "
        "made the first flights. I wish they’d come and take me away.\n"
        "You: What is the meaning of life?\n"
        "Marv: I’m not sure. I’ll ask my friend Google."
    ],
    prompt_template=lambda input: f"You: {input['text']}\nMarv:",
    task=TaskType.qa_open_domain,
)


class ConversationPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="Open ended conversation with an AI assistant.",
            creator="OpenAI",
            homepage="https://beta.openai.com/examples/",
            reference="",
            codebase_url="https://beta.openai.com/examples/",
            license=LicenseType.no_license,
            research_tasks=[TaskType.qa_open_domain],
            application_categories=[ApplicationCategory.conversation],
            application_subcategories=[ApplicationSubcategory.open_ended_conversation],
            original_platform=PlatformType.gpt3,
            design_pattern=DesignPatternType.standalone,
            source_language=LanguageType.en,
            target_language=LanguageType.en,
        )

    def _kernel_configs(self):
        return {
            "openai1": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=150,
                temperature=0.9,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
            ),
            "openai2": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=60,
                temperature=0.5,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0,
            ),
            "openai3": PLMKernelConfig(
                platform="openai",
                model_name="text-curie-001",
                max_tokens=60,
                temperature=0.5,
                top_p=0.5,
                frequency_penalty=0.5,
                presence_penalty=0,
            ),
        }

    def execute(self, input):
        openai_kernel1 = self.kernel_configs["openai1"].to_kernel()
        openai_kernel2 = self.kernel_configs["openai2"].to_kernel()
        openai_kernel3 = self.kernel_configs["openai3"].to_kernel()

        if self.config_name == "default" or self.config_name == "general":
            code = self.get_code(input, self.software_configs["conversation_general"])
            return self.normalize_output(openai_kernel1.execute(code)["text"])

        elif self.config_name == "friend":
            code = self.get_code(input, self.software_configs["conversation_friend"])
            return self.normalize_output(openai_kernel2.execute(code)["text"])
        elif self.config_name == "sarcastic":
            code = self.get_code(input, self.software_configs["conversation_sarcastic"])
            return self.normalize_output(openai_kernel3.execute(code)["text"])
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")

    def _software_configs(self):
        if self.config_name == "default" or self.config_name == "general":
            return {"conversation_general": conversation_general}
        elif self.config_name == "friend":
            return {"conversation_friend": conversation_friend}
        elif self.config_name == "sarcastic":
            return {"conversation_sarcastic": conversation_sarcastic}
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")

    def _example(self):
        if self.config_name == "default" or self.config_name == "general":
            return {
                "input": {"text": "I'd like to cancel my subscription."},
                "output": "Certainly, cancel your subscription anytime you"
                " like. We hope you enjoy using our services!",
            }
        elif self.config_name == "friend":
            return {
                "input": {"text": "I'd like to cancel my subscription."},
                "output": "No problem!",
            }
        elif self.config_name == "sarcastic":
            return {
                "input": {"text": "I'd like to cancel my subscription."},
                "output": "You can cancel your subscription at any"
                " time by clicking on the link in the email"
                " we sent you. Thanks for using Marv!",
            }
        else:
            raise ValueError("Unknown question answer type: {self.config_name}")
