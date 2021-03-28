
# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
sys.path.insert(0, '../mel.utils.providers')
sys.path.insert(1, '../mel.utilities')
sys.path.insert(2, '../mel.procedures')

#STARTED PROGRAM HERE

import os 
import melPropertiesFile
from melJsonProvider import melJsonProvider
import json

class melJsonParser: 
    def _init_ (self)
    pass

def getJsonFile (self, path, fileName): 
    path = melPropertiesFile.melJsonProvider_CONFIG ['path']
    fileName = melPropertiesFile.melJsonProvider_CONFIG ['filenName']
    
    jsonFile = melJsonProvider.getJsonFile (path, fileName)