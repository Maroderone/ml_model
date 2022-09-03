import pickle
import re
import random
import sys

def generate(model, length, seed=42, prefix = None):
        with open(f'{model}', 'rb') as f:
            grams = pickle.load(f)
        if prefix is None:
            prefix = random.choice(list(grams.values())[:-1])[0]
        text=''
        random.seed = seed
        print(grams)
        for i in range(length):
            next_word = random.choice(grams[prefix])
            text += ' '
            text += next_word
            prefix = next_word
        print(text)
