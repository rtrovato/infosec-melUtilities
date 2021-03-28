# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
sys.path.insert(0, '../mel.utils.providers')
sys.path.insert(1, '../mel.utilities')
sys.path.insert(2, '../mel.procedures')

#STARTED PROGRAM HERE
import json


class melJsonProvider:
    ''' Hi I am provider to load & validate and json provider
        Who depends me 
            melJsonParse.py is on
    '''
    def _init_ (self): 
        pass
    
    def getJsonFile (path, filename):
        jsonfile = json.loads(path+"\\"+filename)

        return jsonfile()
    
    
    