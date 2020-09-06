import pickle
import re
import collections

with open("data.pkl", "rb") as data:
    data.seek(0)
    res=pickle.load(data)

array = str(res).split("), (")

password={}
username={}

for item in array:
        if "pass" in item:
                sanitise = re.search(", '(.*)'", item)
                letter = sanitise.group(1)
                sanitise = re.search("ssh_pass(.*)',", item)
                number = sanitise.group(1)
                password[int(number)] = letter
        else:
                sanitise = re.search(", '(.*)'", item)
                letter = sanitise.group(1)
                sanitise = re.search("ssh_user(.*)',", item)
                number = sanitise.group(1)
                username[int(number)] = letter

username = collections.OrderedDict(sorted(username.items()))
password = collections.OrderedDict(sorted(password.items()))

print("Username: ", end = '')
for a, b in username.items(): print(b, end = '')
print("\nPassword: ", end = '')
for a, b in password.items(): print(b, end = '')
print("\n")