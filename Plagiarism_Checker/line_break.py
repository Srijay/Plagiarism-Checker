import shutil
import os

def fun(inputFile,delim):
  infile = open(inputFile, "r")
  outfile = open("out.txt", "w")
  for line in infile:
    line = line.replace("\n","")
    splitted = line.split(delim);
    for i in splitted:
      if(i.rstrip()):
        i = i.replace(" ","")
        outfile.write(i+"\n")
  outfile.close()
  infile.close()
  shutil.copyfile("out.txt",inputFile)
  os.remove("out.txt")

