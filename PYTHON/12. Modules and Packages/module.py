import re

# Your code goes here
find_members = []



for member in dir(re):
    if ("find" in member):
        find_members.append(member)


print(find_members)