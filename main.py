# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    if w in data.keys():
        return  data[w]
    elif w.title() in data.keys():
        return data[w.title()]
    elif w.upper() in data.keys():
        return data[w.upper()]
    else:
        proposiotion=get_close_matches(w,data.keys(),5,0.8)
        if len(proposiotion)>0:
            y_n=input(f"Maybe you wanted one of there words {proposiotion}:\nYes or No? ")
            if y_n.lower()=='yes':
                w=input("Choose the word: ")
                while w not in proposiotion:
                    w = input("Choose the word: ")
                return data[w]

        w=input("Choose a new word or enter \end to exit: ")
        if w=='\end':
            exit()
        return translate(w)

if __name__=='__main__' :
    word=input("Please enter a word: ")
    for x in translate(word.lower()):
         print(x)
