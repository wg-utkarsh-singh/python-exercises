checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]

with open("countries_missing.txt") as f:
    content = f.readlines()
    ulist = sorted(checklist + content)
    with open("countries_missing_fixed.txt", "w") as f2:
        for i in ulist:
            f2.write(i)
