#! /home/efe/anaconda3/bin/python3

import sys

pattern = "abaabc"

string = "dog cat dog dog cat mouse fish"

words = string.split()

match = True
if len(pattern) == len(words):
    pattern_to_word_map = {}
    for i in range(len(pattern)):
        try:
            if pattern_to_word_map[pattern[i]] != words[i]:
                match = False
                break;
        except:
            pattern_to_word_map[pattern[i]] = words[i]
else:
    match = False

print(match)

