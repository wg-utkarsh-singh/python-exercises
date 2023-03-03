import time

i = 0
while True:
    print("Hello")
    i += 1
    if i > 3:
        print("EOL")
        break
    time.sleep(i)
