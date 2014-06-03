#!/usr/bin/env python3

import argparse
import collections
import itertools


DEFAULT_DICT_FILE = '/usr/share/dict/words'


def word_to_sorted_anagram(word):
    """Transform a word into its sorted anagram, e.g. 'cat' becomes 'act'"""
    return ''.join(sorted(word))


class Searcher(object):
    """Searcher class"""

    def __init__(self, fp):
        # Build a lookup table by making each word's sorted anagram point to
        # the original word.
        self.table = collections.defaultdict(list)
        for line in fp:
            word = line.strip().lower()
            key = word_to_sorted_anagram(word)
            self.table[key].append(word)

    def lookup(self, letters, n_letters):
        # Try all combinations of the input. Consult the lookup table for
        # each combo to see whether it points to a known word (or multiple
        # known words).
        answers = set()
        for combo in itertools.combinations(letters, n_letters):
            key = word_to_sorted_anagram(combo)
            value = self.table.get(key)
            if value is not None:
                answers.update(value)

        return answers


def main():
    # Parse command line.
    parser = argparse.ArgumentParser()
    parser.add_argument('--dict', default=DEFAULT_DICT_FILE,
                        help="path to word list file")
    parser.add_argument('n_letters', type=int,
                        help="number of letter in word to guess")
    parser.add_argument('letters', help="all possible letters")
    args = parser.parse_args()

    with open(args.dict) as fp:
        searcher = Searcher(fp)

    answers = searcher.lookup(args.letters, args.n_letters)

    if not answers:
        print("No answers found.")
    else:
        print("Possible answers:")
        for n, word in enumerate(sorted(answers), 1):
            print("{:3d}. {}".format(n, word))


if __name__ == '__main__':
    main()
