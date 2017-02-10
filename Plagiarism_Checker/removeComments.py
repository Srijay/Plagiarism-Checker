import shutil
import os

def singleComment(inputFile,marker):
  infile = open(inputFile, "r")
  outfile = open("out.txt", "w")
  for line in infile:
        line = line.replace("\n","")
	i=line.find(marker)
	if i !=- 1:
		line=line[:i]
        outfile.write(line+"\n")
  outfile.close()
  infile.close()
  shutil.copyfile("out.txt",inputFile)
  os.remove("out.txt")

def blogComment(inputFile,startMarker,endMarker):
  infile = open(inputFile, "r")
  outfile = open("out.txt", "w")
  start_mark_found=False
  for line in infile:
    if start_mark_found==False:
      i=line.find(startMarker)
      if i !=- 1:
	start_mark_found=True
	outfile.write(line[:i]+"\n")
      else:
        if((line != "\n") and (line != "")):
	  outfile.write(line + "\n")
    else:
      j=line.find(endMarker)
      if j != -1:
        start_mark_found= False
	outfile.write(line[j+len(endMarker):]+"\n")
  outfile.close()
  infile.close()
  shutil.copyfile("out.txt",inputFile)
  os.remove("out.txt")
  