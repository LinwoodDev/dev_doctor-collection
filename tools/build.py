#!/usr/bin/env python3
import os
import json

users = os.listdir('metadata')
print("Building data files...")
users = list(filter(lambda user: os.path.isdir(os.path.join('metadata', user)), users))
for user in users:
    entries = {}
    current = os.path.join('metadata', user)
    for item in os.listdir(current):
        if(item != "data.json"):
            with open(os.path.join(current, item), "r") as f:
                data = json.load(f)
                entries[os.path.splitext(item)[0]] = data['url']
    with open(os.path.join(current, "data.json"), "w") as f:
        json.dump({'entries': entries}, f, ensure_ascii=False, indent=4)
    print(user)
with open(os.path.join('metadata', 'data.json'), "w") as f:
    json.dump(users, f, ensure_ascii=False, indent=4)

print("Successfully built data files.")
