import os
import sys 
import datetime 
from mel.config import melPropertiesFile
from mel.services.melDBFuncionarios import melDBFuncionarios
from mel.services.melDBReviewResult import melDBReviewResult
from mel.services.melCsvParser import melCsvParser


class Funcionario:
    def _init_(self): 
        pass 
    
    def getMail(self, user_id):
        funcionario = melDBFuncionarios.getFuncionario("",user_id)
        for i in funcionario: 
            return(str(i[4]))
    
    def getManagerCod(self, user_id):
        path = melPropertiesFile.melStartReviewHereCSV_CONFIG['path']
        arquivo = melPropertiesFile.melStartReviewHereCSV_CONFIG['fileName']
        f = melCsvParser.getSingleCsvFile("",path, arquivo)
        userid = user_id 
        for i in f:
            x = str(i['user_id'])
            if x == userid:
                return (str(i['user_manager']))
        
    def getUserStatus(self, user_id):
        path = melPropertiesFile.melStartReviewHereCSV_CONFIG['path']
        arquivo = melPropertiesFile.melStartReviewHereCSV_CONFIG['fileName']
        f = melCsvParser.getSingleCsvFile("",path, arquivo)
        userid = user_id 
        for i in f:
            x = str(i['user_id'])
            if x == userid:
                return (str(i['user_state']))
            
    
class Revisao: 
    def _init_(self): 
        pass
    
    def validaAtributo (self, atributo): 
        atributo = str(atributo)
        if not atributo: 
            return Null
        else:
            return atributo 
        
    def getUltimaRevisao (self):
        ultimarevisao = melDBReviewResult.getUltimaRevisao("")
        strUltimaRevisao = ultimarevisao[0]
        for x in strUltimaRevisao:
            strRevisao=(str(x))
        return strRevisao
    
    def setRevisao(self, db_review_id, dbname, db_owner_mail, db_manager_mail, db_classificacao):
        

        str_agora = datetime.datetime.utcnow()
        agora = str_agora.strftime('%Y-%m-%d %H:%M:%S')
        melDBReviewResult.setReviewResult ("",db_review_id, agora, dbname, db_owner_mail, db_manager_mail, db_classificacao)
        

if __name__ == "__main__":
    pass
    
    

    