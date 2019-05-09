#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from collections import Counter
from itertools import permutations
import random
from data import DICTIONARY, LETTER_SCORES, POUCH
from typing import List

NUM_LETTERS = 7

def draw_letters() -> List[str]:
    return random.sample(POUCH, NUM_LETTERS)

def input_word(draw: List[str]) -> str:
    while True:
        word = input("Select a word...\n")
        try:
            _validation(word, draw)
            return word
        except ValueError:
            print("Not valid, choose another word.")

def _validation(word: str, draw: List[str]):
    if word.lower() not in DICTIONARY:
        raise ValueError
    counts = Counter(draw)
    counts.subtract(Counter(word.upper()))
    for count in counts.values():
        if count < 0:
            raise ValueError
    return

# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    return [word for word in _get_permutations_draw(draw) if ''.join(word).lower() in DICTIONARY]


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    perms = list()
    for length in range(1, NUM_LETTERS + 1):
        perms.extend(permutations(draw, length))
    return perms

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    draw = draw_letters()
    print(f"You have drawn: {draw}")
    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))
    


if __name__ == "__main__":
    main()
