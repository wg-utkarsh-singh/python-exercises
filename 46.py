from glob import glob

letters = []
fnames = glob("letters/*.txt")

for fname in fnames:
    with open(fname) as f:
        letters.append(f.read().strip("\n"))

print(letters)
