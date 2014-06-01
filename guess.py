#!/usr/bin/env python3

import argparse
import collections
import itertools


DEFAULT_DICT_FILE = '/usr/share/dict/words'


def word_to_sorted_anagram(word):
    """Transform a word into its sorted anagram, e.g. 'cat' becomes 'act'"""
    return ''.join(sorted(word))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dict', default=DEFAULT_DICT_FILE,
                        help="path to word list file")
    parser.add_argument('n_letters', type=int,
                        help="number of letter in word to guess")
    parser.add_argument('letters', help="all possible letters")
    args = parser.parse_args()

    words_by_anagram = collections.defaultdict(list)
    with open(args.dict) as fp:
        for line in fp:
            word = line.strip().lower()
            key = word_to_sorted_anagram(word)
            words_by_anagram[key].append(word)

    possible_answers = []
    for combo in itertools.combinations(args.letters, args.n_letters):
        key = word_to_sorted_anagram(combo)
        value = words_by_anagram.get(key)
        if value is not None:
            possible_answers.extend(value)

    possible_answers = sorted(set(possible_answers))
    if not possible_answers:
        print("No answers found.")
    else:
        print("Possible answers:")
        for n, word in enumerate(possible_answers, 1):
            print("{:3d}. {}".format(n, word))


if __name__ == '__main__':
    main()
