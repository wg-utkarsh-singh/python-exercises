from os import makedirs
from os.path import exists
from string import ascii_lowercase

if not exists("letters"):
    makedirs("letters")

for l in ascii_lowercase:
    with open(f"letters/{l}.txt", "w") as f:
        f.write(f"{l}\n")
