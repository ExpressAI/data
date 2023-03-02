# Software: `softwares/essay_outline`

This promptware is used to generate an outline for a research topic.

```python
import promptware
software = promptware.install("essay_outline")
output = software.execute("Create an outline for an essay about Nikola Tesla and his contributions to technology:")
# output:
# I. Introduction
# A. Definition of Nikola Tesla
# B. Overview of Tesla's life and accomplishments
# 
# II. Early Life and Education
# A. Tesla's birthplace and family
# B. Tesla's education and early career
# 
# III. Contributions to Technology
# A. Alternating current
# B. Radio and remote control
# C. Robotics and artificial intelligence
# D. X-rays and lasers
# 
# IV. Legacy of Tesla
# A. Impact on modern technology
# B. Recognition of Tesla's work
# 
#  V. Conclusion
# A. Summary of Tesla's life and accomplishments
# B. Reflection on Tesla's legacy
```