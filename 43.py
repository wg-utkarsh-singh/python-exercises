from string import ascii_lowercase

with open("letters.txt", "w") as f:
    for l1, l2 in zip(ascii_lowercase[::2], ascii_lowercase[1::2]):
        f.write(f"{l1} {l2}\n")
