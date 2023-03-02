# Software: `softwares/headline_generation`

This software is used to generate headline for a news article with different styles

```python
import promptware
software = promptware.install("headline_generation")
output = software.execute("传统生活方式相关的风险因素，包括吸烟、过度饮酒、缺乏运动、不良饮食习惯和肥胖，与死亡风险增加有关，尤其是慢性病。然而，只有少数研究评估了个人生活方式因素（如吸烟和饮酒）对中国人口预期寿命的影响。综合生活方式行为对中国人预期寿命的影响尚不清楚，需要填补证据空白。2022年8月1日，北京大学李立明、吕筠与中国疾病预防控制中心赵丽云团队在 Lancet Public Health (IF=72) 期刊在线发表题为“Healthy lifestyle and life expectancy at age 30 years in the Chinese population: an observational study”的研究论文，该研究调查了健康生活方式对中国人30岁时预期寿命影响。五种低风险生活方式：从不吸烟或戒烟、不过度饮酒、积极运动、健康的饮食习惯和健康的体型）中，与五种生活方式均低风险和只有一个或没有低风险的个体相比，男性在30岁时的预期寿命延长8.8年（95% CI 6.8-10.7），女性为8.1年（6.5–9.9）。该研究结果表明，通过公共卫生干预这五种健康生活方式可能会大幅延长中国人口的预期寿命。")
# output:
# 中国人，不只要“吃”！这5种生活方式，可延寿8-9年
```