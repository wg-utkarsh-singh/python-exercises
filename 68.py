d = dict(weather="clima", earth="terra", rain="chuva")


def vocabulary(word):
    return d.get(word, "We couldn't find that word!")


word = input("Enter word: ").lower()
print(vocabulary(word))
