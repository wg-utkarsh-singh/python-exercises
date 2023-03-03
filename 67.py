d = dict(weather="clima", earth="terra", rain="chuva")


def vocabulary(word):
    return d.get(word, "The word does not exist.")


word = input("Enter word: ")
print(vocabulary(word))
