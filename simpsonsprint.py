#!/usr/bin/python3
#My eyes, the goggles do nothing
easy= ["science", "turbo", ["goggles", "eyes"], "nothing"]


medium= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


hard= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print(f"My {easy[2][1]} the {easy[2][0]} do {easy[3]}")
print(f"My {medium[2]['goggles']} the {medium[2]['eyes']} do {medium[3]}")
print(f"My {hard[0]['user']['name']['first']} the {hard[0]['kumquat']} do {hard[0]['d']}")
