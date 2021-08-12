from os import path
import pip


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', termcolor])
    else:
        pip._internal.main(['install', termcolor])

from termcolor import colored


pathToCauseFile = "/Users/oishikachaudhury/Downloads/AFP_ENG_20021112.0724.cause"
colorsList = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]



readFile = open(pathToCauseFile)
for line in readFile:
    count = 0
    listOfWords = line.split("\t")
    for word in listOfWords:
        print(colored(word,colorsList[count%len(colorsList)]), end = " ")
        count  += 1
    print("\n\n")
