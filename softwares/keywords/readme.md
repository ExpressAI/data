# Software: `softwares/keywords`

This promptware is used to extract keywords from a block of text. At a lower temperature it picks keywords from the text. At a higher temperature it will generate related keywords which can be helpful for creating search indexes.

```python
import promptware
software = promptware.install("keywords")
output = software.execute("Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors.")
# output:
# Keywords: black-on-black ware, 20th century, 21st century, Puebloan Native American, ceramic artists, Northern New Mexico, reduction-fired blackware, pueblo artists, burnishing/ slip/carving/incising designs/polishing
```