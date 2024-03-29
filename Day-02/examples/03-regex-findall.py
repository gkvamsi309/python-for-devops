import re

text = "The quick brown fox if brown is found.Then brown should should be deleted"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
