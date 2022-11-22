from __future__ import annotations

from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware
from promptware.tasks import TaskType


class HeadlineGenerationPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="This software is used to generate headline for a news "
            "article with different styles",
            creator="Promptware Authors",
            homepage="https://github.com/expressai/promptware",
            reference="",
            codebase_url="https://github.com/expressai/promptware/tree/main/softwares",
            license=LicenseType.apache_2_0,
            task=TaskType.conditional_generation,
        )

    def _kernel_configs(self):
        return {
            "openai": PLMKernelConfig(
                platform="openai",
                model_name="text-davinci-002",
                max_tokens=64,
                temperature=0,
                top_p=1,
            )
        }

    def _software_configs(self):
        return {
            "headline_generation": PromptConfig(
                name="headline_generation",
                description="This software is used to generate headline for a news "
                "article with different styles",
                instruction="给定一个新闻文章，我们生成一个足够吸引人的标题",
                demonstration=[
                    "新闻：\n近日，现年47岁的新晋中国科学院院士、武汉大学教授宋保亮团队于"
                    "Nature（《自然》）杂志**发表论文，发现促使胆固醇外排而降脂的全新策略"
                    "。2021年11月，宋保亮当选中国科学院院士，时年46岁，成为当届当选的最年"
                    "轻院士之一。宋保亮教授曾在武大研究生开学典礼上演讲，用自己的成长发展经"
                    "历激励广大研究生，并提出快速融入研究生生活的六个建议。\n标题：\n47岁"
                    "院士再发Nature！他给研究生的这6个建议流传甚广",
                    "新闻：\n日前，教育部官网发布《关于河北工程技术学院等四所民办本科学校"
                    "变更举办者、办学地址的公示》。《公示》透露：西南交通大学希望学院办"
                    "学地址由“四川省南充市嘉陵区于陛路”变更为“四川省成都市金堂县学府大"
                    "道558号”。\n标题：又一高校，迁至省会办学！",
                    "新闻：\nDichtel、加利福尼亚大学洛杉矶分校K. N. Houk院士及中国科学院"
                    "上海有机化学研究所薛小松等多团队合作（西北大学Brittany Trang和天津"
                    "大学Li Yuli是共同第一作者）在Science在线发表题为“Low-temperature"
                    " mineralization of perfluorocarboxylic acids”的研究论文，该研究"
                    "发现全氟烷基羧酸 (PFCA) 可以通过氢氧化钠介导的脱氟途径进行矿化"
                    "。值得注意的是，天津大学理学院2018级本科生李预立作为共同第一作者，"
                    "而他是一名“00后”。\n标题：\n硬核！“00后”本科生，一作发Science！",
                    "新闻：\n8月16日，正值太原理工大学喜迎纪念建校120周年之际，中国科学院"
                    "19名院士及专家一行到太原理工大学明向校区考察调研，校党委书记郑强"
                    "等校领导陪同调研座谈。\n标题：\n大动作！19位院士，调研太原理工",
                ],
                prompt_template=lambda input: f"新闻：\n{input['text']}\n标题：\n",
                task=TaskType.conditional_generation,
            )
        }
