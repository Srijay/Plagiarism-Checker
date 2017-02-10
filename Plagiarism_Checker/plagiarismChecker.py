#!/usr/bin/python
import os.path
import shutil
import sys
import plagiarismCheckerHelper
import operator

def AskForFeatures(tmpDir,tmpFile):
  print "Do you want to remove cases Y or N?\n"
  d = raw_input()
  if((d == 'Y') or (d == 'y')):
    plagiarismCheckerHelper.removeCases(tmpFile,tmpDir)
    
  print "Do you want to apply line break?\n" 
  d = raw_input()
  if((d == 'Y') or (d == 'y')):
    print "Enter the line breaker\n"
    lineMarker = raw_input()
    plagiarismCheckerHelper.applyLineBreak(tmpFile,tmpDir,lineMarker)
    
  print "Now Say, do you want to remove comments?\n"
  d = raw_input()
  if((d == 'Y') or (d == 'y')):
    print "If single line comment, press 's' if blog comment required, press 'b'\n"
    c = raw_input()
    if(c == 's'):
      print "Enter the marker\n"
      singleMarker = raw_input()
      plagiarismCheckerHelper.removeSingleComments(tmpFile,tmpDir,singleMarker)
    if(c=='b'):
      print "Enter the startMarker and endMarker\n"
      startMarker = raw_input()
      endMarker = raw_input()
      plagiarismCheckerHelper.removeBlogComments(tmpFile,tmpDir,startMarker,endMarker)
  return

def catchPlagiarism(checkFile,dirName,output):

  tmpDir = "tmpDir"
  tmpFile = "tmpFile"
  
  shutil.copytree(dirName,tmpDir,symlinks=False,ignore=None)
  shutil.copyfile(checkFile,tmpFile)
    
  print ""
  print "Hi Welcome to Plagirsm Checker\n"
  print "Think of the Feature that you want to implement\n"
  
  AskForFeatures(tmpDir,tmpFile)
  
  checkFileArray = plagiarismCheckerHelper.getFileInArray(tmpFile)
        
  print "Here we check if anybody has copied and print filenames as per copied index\n"                               
  print "File to be checked - " + checkFile + "\n"
  
  result = {}      
                                        
  for inpfile in os.listdir (tmpDir):
    similarIndex = 0
    inFileArray = plagiarismCheckerHelper.getFileInArray(tmpDir + '/'+inpfile)
    similarIndex = plagiarismCheckerHelper.getSimilarIndex(checkFileArray,inFileArray)
    result[inpfile] = similarIndex
    
  os.remove(tmpFile)
  shutil.rmtree(tmpDir)
  
  sorted_result = sorted(result.items(), key=operator.itemgetter(1))
  plagiarismCheckerHelper.writeResultIntoFile(sorted_result,output)
  return
  
  
  