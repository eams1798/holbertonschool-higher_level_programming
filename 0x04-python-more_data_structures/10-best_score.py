#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best = 0
    for s in a_dictionary:
        score = a_dictionary[s]
        if score > best:
            best = score
            return best
