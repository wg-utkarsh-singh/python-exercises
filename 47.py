import glob

letters = []
file_list = glob.iglob("letters/*.txt")
check = "python"

for filename in file_list:
    with open(filename, "r") as file:
        letter = file.read().strip("\n")
    if letter in check:
        letters.append(letter)

print(letters)
