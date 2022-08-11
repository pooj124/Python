with open("mine.log", 'r') as f:
    for line in f:
        if "Mul" in line:
            print(line)