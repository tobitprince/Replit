"""
Clean File
"""
import re

with open('testing.txt', 'r', encoding="utf-8") as file:
    content = file.read()
#remove unwanted elements
# Remove unwanted elements using regular expressions
# \b(ORIGIN|1|61)\b matches whole words ORIGIN, 1, and 61
# |// matches the // sequence
# |\s+ matches any whitespace characters (spaces, tabs, newlines)
cleaned_content = re.sub(r'\b(ORIGIN|1|61)\b|//|\s+', '', content)

#save the contents
with open('preproinsulin-seq-clean.txt', 'w', encoding="utf-8") as file:
    file.write(cleaned_content)

#verifying total length  
assert len(cleaned_content) == 110, f"Expected 110 characters , got {len(cleaned_content)}"

lsinsulin_seq = cleaned_content[0:24]
binsulin_seq = cleaned_content[24:54]
cinsulin_seq = cleaned_content[54:89]
ainsulin_seq = cleaned_content[89:110]

#verifying
assert len(lsinsulin_seq) == 24, f"Expected 24 Characters, got {len(lsinsulin_seq)}"
assert len(binsulin_seq) == 30, f"Expected 30 characters , got {len(binsulin_seq)}"
assert len(cinsulin_seq) == 35, f"Expected 35 characters , got {len(cinsulin_seq)}"
assert len(ainsulin_seq) == 21, f"Expected 21 characters , got {len(ainsulin_seq)}"

#saving the contents to the files
with open('lsinsulin-seq-clean.txt', 'w', encoding="utf-8") as file:
    file.write(lsinsulin_seq)

with open('binsulin-seq-clean.txt', 'w', encoding="utf-8") as file:
    file.write(binsulin_seq)

with open('cinsulin-seq-clean.txt', 'w', encoding="utf-8") as file:
    file.write(cinsulin_seq)

with open('ainsulin-seq-clean.txt', 'w', encoding="utf-8") as file:
    file.write(ainsulin_seq)

print("Files verified and saved successfully")
