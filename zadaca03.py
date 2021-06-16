import re

string = str(input("Unesi string: "))
string = string.lower()

regex = "^m.*[0-5]\s.*č$"

result = re.findall(regex, string)

if result:
    print("Podudaranje")

else:
    print("Nema podudaranja")
