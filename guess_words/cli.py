import argparse

from guess_words import search

DEFAULT_DICT_FILE = '/usr/share/dict/words'


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
        searcher = search.Searcher(fp)

    answers = searcher.lookup(args.letters, args.n_letters)

    if not answers:
        print("No answers found.")
    else:
        print("Possible answers:")
        for n, word in enumerate(sorted(answers), 1):
            print("{:3d}. {}".format(n, word))


if __name__ == '__main__':
    main()
