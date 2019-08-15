#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from collections import Counter
from itertools import permutations
import random
from data import DICTIONARY, LETTER_SCORES, POUCH
from typing import List, Iterator, Tuple

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

def _validation(word: str, draw: List[str]) -> None:
    if word.lower() not in DICTIONARY:
        raise ValueError
    counts = Counter(draw)
    counts.subtract(Counter(word.upper()))
    for count in counts.values():
        if count < 0:
            raise ValueError
    return

class Draw():
    def __init__(self):
        self.letters = draw_letters()
    
    def get_possible_dict_words(self) -> List[str]:
        """Get all possible words from draw which are valid dictionary words."""
        return [
            ''.join(word) for word in self._get_permutations()
            if ''.join(word).lower() in DICTIONARY
        ]

    def _get_permutations(self) -> Iterator[Tuple]:
        for length in range(1, NUM_LETTERS + 1):
            yield from permutations(self.letters, length)

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    draw = Draw()
    print(f"You have drawn: {draw.letters}")
    word = input_word(draw.letters)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = draw.get_possible_dict_words()

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))
    


if __name__ == "__main__":
    main()
