###--- IMPORTS ---###
import collections


###--- FUNCTIONS ---###
def count_words():
    with open('Transcript.txt', 'rt') as t:
        data = t.read()
        words = data.split()
        word_count = collections.Counter(words)
        print(word_count)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    count_words()
