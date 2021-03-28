# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
sys.path.insert(0, '../mel.utils.providers')
sys.path.insert(1, '../mel.utilities')
sys.path.insert(2, '../mel.procedures')

#STARTED PROGRAM HERE
import csv

class melCsvProvider:
    ''' Hi I am provider to load & validate and json provider
        Who depends me 
            melJsonParse.py is on
    '''
    def _init_ (self): 
        pass
    
    def getCsvFile (path, filename):
        try:
            
            file_to_open = path+filename
            with open (file_to_open, 'r') as txtfile:
                csvfile = csv.reader(txtfile, delimiter=',')
                csvobj = list() 
                for row in csvfile: 
                    csvobj.append(row)
                objcsv = [dict(zip(csvobj[0],row)) for row in csvobj]
                objcsv.pop(0)
                return objcsv  
    
        except Exception as e:
            print (str(e))

    
    