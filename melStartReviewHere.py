
# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
sys.path.insert(0, './mel.utils.providers')
sys.path.insert(1, './mel.utilities')
sys.path.insert(2, './mel.procedures')

#STARTED PROGRAM HERE
import os
import json
from melJsonParser import melJsonParser
import melPropertiesFile


def __main__(): 
    try: 
        getDBtoReview() 
    except Exception as e:
        print (str(e))

def getDBtoReview(): 
    path =      melPropertiesFile.melStartReviewHere_CONFIG ['path']
    fileName =  melPropertiesFile.melStartReviewHere_CONFIG ['fileName']
    
    melDBtoReview   = melJsonParser.getSingleJsonFile ("", path, fileName)
    melUserManager  = melcsvParser.getSingleCsvFile("")
    
    for i in (melDBtoReview):
        pass
       
if __name__ == "__main__":
    
    __main__()
