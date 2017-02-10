import shutil
import os
import edit_distance
import remove_case
import line_break
import removeComments

def getFileInArray(filename):  
  infile = open(filename, "r")
  array = []
  for line in infile:
    line = line.replace("\n","")
    line = line.replace(" ","")
    array.append(line)
    if "" in array:     
      array.remove("")
  return array
  
def getSimilarIndex(check,inp):
  dist = 0
  for i in check:
    min = len(i)
    for j in inp:
      editdistance = edit_distance.computeDistance(i,j)
      if(editdistance < min):
        min = editdistance
    dist = dist + min
  return dist

def removeCases(checkFile,dirName):
  remove_case.fun(checkFile)
  for inpfile in os.listdir (dirName):
    remove_case.fun(dirName+'/'+inpfile)

def applyLineBreak(checkFile,dirName,breaker):
  line_break.fun(checkFile,breaker)
  for inpfile in os.listdir (dirName):
    line_break.fun(dirName+'/'+inpfile,breaker)

def removeSingleComments(checkFile,dirName,marker):
  removeComments.singleComment(checkFile,marker)
  for inpfile in os.listdir (dirName):
    removeComments.singleComment(dirName+'/'+inpfile,marker)

def removeBlogComments(checkFile,dirName,startMarker,endMarker):
  removeComments.blogComment(checkFile,startMarker,endMarker)
  for inpfile in os.listdir (dirName):
    removeComments.blogComment(dirName+'/'+inpfile,startMarker,endMarker)
    
def writeResultIntoFile(result,outputfile):
  out = open(outputfile, "w")
  out.write("FileName  PlagiarismIndex\n")
  for entry in result:
    out.write(entry[0] + "           " + str(entry[1]) + "\n")