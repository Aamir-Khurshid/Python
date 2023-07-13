import re
pattern = r"[A-Z]"
text = '''How are you? Its been a long day'''
#print(re.search(pattern,text))
match = re.finditer(pattern,text)
for matching in match:
    print(matching.span())
    print(text[matching.span()[0]:matching.span()[1]])
