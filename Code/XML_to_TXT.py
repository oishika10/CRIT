filename = input()
fileRead =  open(filename)
fileWrite = open(filename[:-4]+".txt", "a")


for line in fileRead:
    found = line.find("<p>")
    if found != -1:
        fileWrite.write(line[found+3:-6])
        fileWrite.write("\n")
    else:
        pass
