# Software: `softwares/science_fiction_book_list_maker`

This promptware is used to make a list of science fiction books and stop when it reaches #10.

```python
import promptware
software = promptware.install("science_fiction_book_list_maker")
output = software.execute("List 10 science fiction books:")
# output:
# 1. 1984 by George Orwell
# 2. Dune by Frank Herbert
# 3. The Hitchhiker's Guide to the Galaxy by Douglas Adams
# 4. The War of the Worlds by H.G. Wells
# 5. Brave New World by Aldous Huxley
# 6. Ender's Game by Orson Scott Card
# 7. The Martian Chronicles by Ray Bradbury
# 8. Do Androids Dream of Electric Sheep? By Philip K Dick 
# 9. Snow Crash by Neal Stephenson 
# 10. Neuromancer by William Gibson
```