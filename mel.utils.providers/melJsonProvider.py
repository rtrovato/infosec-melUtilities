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
        try:
            
            file_to_open = path+filename
            with open (file_to_open, 'r') as txtfile:
                jsonfile    = txtfile.read();
                jsonobj     = json.loads(jsonfile)
                return jsonobj 
            
        except Exception as e:
            print (str(e))

    
    