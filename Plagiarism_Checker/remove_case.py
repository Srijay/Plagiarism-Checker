import shutil
import os

def fun(inputFile):
  infile = open(inputFile, "r")
  outfile = open("out.txt", "w")
  for line in infile:
    line = line.replace("\n","")
    if(line.rstrip()):
      line = line.replace(" ","")
      outfile.write(line.lower()+"\n")
  outfile.close()
  infile.close()
  shutil.copyfile("out.txt",inputFile)
  os.remove("out.txt")
