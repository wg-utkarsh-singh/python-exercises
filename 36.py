def count_words(filepath):
    with open(filepath, "r") as file:
        strng = file.read()
        return len(strng.split(" "))


print(count_words("words1.txt"))
