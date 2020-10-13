import random


def spongebob(str): return ''.join(
    [l.upper() if random.choice([1, 0]) else l.lower() for l in str])


spongebob('i made a script that randomly capitalizes letters in a sentence')
