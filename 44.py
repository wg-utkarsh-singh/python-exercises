from string import ascii_lowercase as lc

with open("letters.txt", "w") as f:
    for l1, l2, l3 in zip(lc[::3], lc[1::3], lc[2::3]):
        f.write(f"{l1} {l2} {l3}\n")
