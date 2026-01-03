#!/usr/bin/python3

import random
from collections import Counter
import re
from pathlib import Path

path = Path("./100-days-of-python-m/day_1/english_words.txt").expanduser()

print("Welcome to the Band Name Generator.")

city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")

random_name_order_selection = input("Do you want to random shuffle the order of the name of the pet and city? [Yes or No]\n")
full_random = input("Do you want me to find the closes names of english language bases on the letters of the two words? [Yes or No]\n")

if random_name_order_selection.lower() == "yes":
    a, b = random.sample([city_name, pet_name], 2)
    print(f"Your band name could be {a} {b}")
    
if full_random == "yes":
    need_city = Counter(city_name)
    need_pet = Counter(pet_name)
    matches = []
    
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for word in re.findall(r"[A-Za-z]+", line.lower()):
                have = Counter(word)
                if all(have[ch] >= cnt for ch, cnt in need_city.items()):
                    matches.append(word)
                if all(have[ch] >= cnt for ch, cnt in need_pet.items()):
                    matches.append(word)
    
    check_size_ok = len(matches)
    if check_size_ok < 2:
        print(f"The english dictionary is not so complete as the words you have choose.\nTherefore, we will only give you the initial choix.\nYour band name could be {city_name} {pet_name}!")
    else:
        a, b = random.sample(matches, 2)
        print(f"Your band name could be {a} {b}")
    
if random_name_order_selection.lower() == "no" and full_random.lower() == "no":
    print(f"Your band name could be {city_name} {pet_name}!")