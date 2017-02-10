import plagiarismChecker
import sys

dirName = str(sys.argv[1])

checkFile = str(sys.argv[2])
outputFile = str(sys.argv[3])

plagiarismChecker.catchPlagiarism(checkFile,dirName,outputFile)

print "Result is written in file " + outputFile + "\n"