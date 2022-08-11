
with open("mine.log", 'r') as f:
    for line in f:
        if "Add" in line:
            print(line)