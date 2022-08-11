with open("mine.log", 'r') as f:
    for line in f:
        if "Sub" in line:
            print(line)