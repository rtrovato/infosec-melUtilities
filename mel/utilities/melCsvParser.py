
# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
sys.path.insert(0, '../mel.utils.providers')
sys.path.insert(1, '../mel.utilities')
sys.path.insert(2, '../mel.procedures')

#STARTED PROGRAM HERE

import os 
import melPropertiesFile
from 
from melCsvProvider import melCsvProvider
import json

class melCsvParser: 
    def _init_ (self):
        pass

    def getSingleCsvFile (self, path, fileName): 
        melCsvFile = melCsvProvider.getCsvFile(path, fileName)
        return melCsvFile

    

   
    

