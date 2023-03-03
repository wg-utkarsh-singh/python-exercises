with open("countries-raw.txt") as f:
    content = f.readlines()
    content = [i.strip("\n") for i in content if "\n" in i]
    content = [i for i in content if i != "" and i != "Top of Page" and len(i) != 1]
    with open("countries-clean.txt", "w") as f2:
        for i in content:
            f2.write(i + "\n")
