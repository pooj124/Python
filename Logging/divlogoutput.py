with open("mine.log", 'r') as f:
    for line in f:
        if "Div" in line:
            print(line)