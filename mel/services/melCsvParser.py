
import sys 
import os 
import json
from mel.config import melPropertiesFile
from mel.providers.melCsvProvider import melCsvProvider



class melCsvParser: 
    def _init_ (self):
        pass

    def getSingleCsvFile (self, path, fileName): 
        melCsvFile = melCsvProvider.getCsvFile(path, fileName)
        return melCsvFile

    

   
    

