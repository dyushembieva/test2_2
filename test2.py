import re

pattern = re.compile(r'\d+')
result = pattern.findall("12 ай, 12 жыл 12 үй 12 киши")
print(result)


