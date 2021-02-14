#!/usr/bin/env python3
import os
import json

users = os.listdir('metadata')
print("Building data files...")
for user in users:
    items = []
    current = os.path.join('metadata', user)
    for item in os.listdir(current):
        if(item != "data.json"):
            items.append(os.path.splitext(item)[0])
    with open(os.path.join(current, "data.json"), "w") as f:
        json.dump(items, f, ensure_ascii=False, indent=4)
    print(user)
with open(os.path.join('metadata', 'data.json'), "w") as f:
    json.dump(users, f, ensure_ascii=False, indent=4)

print("Successfully built data files.")
