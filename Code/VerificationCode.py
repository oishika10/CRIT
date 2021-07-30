import os
import sys 

cwd = os.getcwd()
oneDirectoryUp = cwd[:cwd.find("Code")]

userInput = input("What file would you like to open? \n")
causeFile = open(oneDirectoryUp + "GLARF Output/" + userInput + ".cause")
annotationFile = open(oneDirectoryUp + "Annotation_Files/" + userInput + ".sgm.sent")


lineNumbers = []
sentencesFromCauseFile = []
for line in causeFile:
  lineNum = line[:line.find("	")]
  lineNumbers.append(lineNum)
  toAdd = line[line.find("	")+1:]
  sentencesFromCauseFile.append(toAdd)


sentencesFromAnnotationFile = []
for lineNumber in lineNumbers:
  for line in annotationFile:
    if lineNumber == line[:line.find(" ")]:
      sentencesFromAnnotationFile.append(line[line.find(" ")+1:])
  annotationFile = open(oneDirectoryUp + "Annotation_Files/" + userInput + ".sgm.sent")


userInputList = []
for i in range(len(sentencesFromCauseFile)):
  print("--------------------" + i + "---------------------")
  print("-----------------------SENTENCE---------------------\n")
  print(sentencesFromAnnotationFile[i])
  print("-----------------------CAUSATION---------------------\n")
  print(sentencesFromCauseFile[i])
  userVerification = input("Is this correct/incorrect?\n")
  userInputList.append(userVerification)
  
