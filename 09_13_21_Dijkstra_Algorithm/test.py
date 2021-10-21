import re

pattern = \
    re.compile(
        r"vị trí sở trường của xxx là( ở đâu| gì)( trên sân)?\s?\??")
string = "vị trí sở trường của xxx là ở đâu trên sân?"

print(re.match(pattern, string))
print(len(string))
# print(re.findall(pattern, string))
