import random as rd
import re

text = "br reg er gr d d d d"
dict = {'one': 1, 'two': 2, 'three': 3}


def returnOneCount(text):
    return len([txt for txt in re.findall(r"[\w']+", text) if len(text) == 1])


print(returnOneCount(text))
