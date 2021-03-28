
import sys 
import os 
import melPropertiesFile
import json
from mel.providers.melJsonProvider import melJsonProvider

class melJsonParser: 
    def _init_ (self):
        
        pass

    def getSingleJsonFile (self, path, fileName): 
        melJsonFile = melJsonProvider.getJsonFile(path, fileName)
        return melJsonFile

    

   
    

