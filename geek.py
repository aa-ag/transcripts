###--- IMPORTS ---###
import collections


###--- FUNCTIONS ---###
def count_words():
    with open('Transcript.txt', 'rt') as t:
        data = t.read()
        words = data.split()
        word_count = collections.Counter(words)
        # All words
        # print(word_count)

        # Selection that meets a conditional
        repetitive_words = {k: v for k, v in word_count.items() if v > 10}
        # print(repetitive_words)
        # {'the': 62, 'of': 36, 'in': 19, 'and': 20, 'a': 47, 'is': 26, 'silicon': 16, 'to': 34, 'with': 12}

        print(dict(sorted(repetitive_words.items(),
                          key=lambda item: item[1], reverse=True)))


###--- DRIVER CODE ---###
if __name__ == "__main__":
    count_words()
