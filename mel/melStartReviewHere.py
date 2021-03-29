
import sys 
import os
import json
import melPropertiesFile


from mel.services.melJsonParser import melJsonParser
from mel.services.melCsvParser import melCsvParser
from mel.services.melSendMail import melSendMail
from mel.services.melDBReviewResult import melDBReviewResult


def __main__(): 
    try: 
        getDBtoReview() 
    except Exception as e:
        print (str(e))

def getDBtoReview(): 
    pathjson =      melPropertiesFile.melStartReviewHereJSON_CONFIG ['path']
    filenamejson =  melPropertiesFile.melStartReviewHereJSON_CONFIG ['fileName']
    
    pathcsv =      melPropertiesFile.melStartReviewHereCSV_CONFIG ['path']
    filenamecsv =  melPropertiesFile.melStartReviewHereCSV_CONFIG ['fileName']
    
    melDBtoReview   = melJsonParser.getSingleJsonFile ("", pathjson, filenamejson)
    melUserManager  = melCsvParser.getSingleCsvFile("", pathcsv, filenamecsv)
    
    for i in (melDBtoReview):
        for u in (melUserManager):
            pass
        
    melSendMail.sendMail("","ricardo.trovato@gmail.com","BANCO_VENDAS","ULTRACONFIDENCIAL","msgok")
    melDBReviewResult.setReviewResult("")
    

if __name__ == "__main__":
    
    __main__()
