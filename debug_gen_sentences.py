
import sys

from hw0 import gen_sentences


def debug_gen_sentences():
    try:
        path = sys.argv[1]
    except IndexError:
        print(
            "You must pass a single command line argument:",
            "python debug_gen_sentences.py <path>",
            sep="\n",
        )
        sys.exit(1)

    for sentence in gen_sentences(path):
        print(sentence)


if __name__ == "__main__":
    debug_gen_sentences()
