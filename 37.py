import re


def count_words_re(filepath):
    with open(filepath, "r") as file:
        text = file.read()
        return len(re.split(",| ", text))


print(count_words_re("words2.txt"))
