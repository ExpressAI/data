# Software: `softwares/spreadsheet_creator`

This promptware is used to create spreadsheets of various kinds of data. It's a long prompt but very versatile. Output can be copy+pasted into a text file and saved as a .csv with pipe separators.

```python
import promptware
software = promptware.install("spreadsheet_creator")
output = software.execute("A two-column spreadsheet of top science fiction movies and the year of release:\n\nTitle |  Year of release")
# output:
# ----------------------------
# Blade Runner  | 1982
# The Matrix | 1999
# Alien | 1979
# The Terminator | 1984
# Back to the Future | 1985
# Star Wars | 1977
# E.T. the Extra-Terrestrial | 1982
# 2001: A Space Odyssey | 1968
# The Day the Earth St
```