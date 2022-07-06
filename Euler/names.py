file = open("names.txt", "r")
for lines in file:
    line = lines.split(",")
    print(line)