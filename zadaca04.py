import re


email = input("Unesi email: ")
regex = "^([a-zA-Z].*)[.]([a-zA-Z].*)@fpmoz.sum.ba$"
result = re.match(regex, email)

edu = input("Unesi eduId: ")
regex1 = "^([a-zA-Z])([a-zA-Z].*)[0-9]*@sum.ba$"
result1 = re.match(regex1, edu)

if result:
    print("Email je tocan")
else:
    print("Email nije tocan")
    
if result1:
    print("eduId je tocan")
else:
    print("eduId nije tocan")
    
