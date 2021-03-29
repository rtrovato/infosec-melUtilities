
import sys 
import os
import json

from mel.config import melPropertiesFile
from mel.services.melJsonParser import melJsonParser
from mel.services.melCsvParser import melCsvParser
from mel.services.melSendMail import melSendMail
## from mel.services.melDBReviewResult import melDBReviewResult
from mel.services.melDataControl import Funcionario, Hierarquia, Revisao

def __main__(): 
    try:
        startDBReview("") 
    except Exception as e:
        print (str(e))

def startDBReview(self): 
    ''' Coletar Informacoes para inciar processamento da revisao'''
    pathjson        =  melPropertiesFile.melStartReviewHereJSON_CONFIG ['path']
    filenamejson =  melPropertiesFile.melStartReviewHereJSON_CONFIG ['fileName']
    melDBtoReview   = melJsonParser.getSingleJsonFile ("", pathjson, filenamejson)
  

    ''' Validar registros e aplicar Regras de negocios ''' 
    
    for databases in melDBtoReview.items():
        ''' R01 - Validar Atributos Nulos '''
        dbName  = Revisao.validaAtributo("",(str(databases[0])))
        dbOwner = Revisao.validaAtributo("",(str(databases[1]['cod_owner'])))
        dbClass = Revisao.validaAtributo("",(str(databases[1]['class'])))
        
        '''R01.1 - Recuperar proximo id para registro da revisao'''
        db_review_id = Revisao.getUltimaRevisao("")
        
        ''' R02 - Se nulo DBOwner nao recuperar registros de CSV
            Neste caso o sistema cai na R03 e envia email para o ADM do Sistem.'''  
        if dbOwner:           
            db_owner_email   = str(Funcionario.getMail("",dbOwner))
            db_manager_id    = str(Funcionario.getManagerCod("",dbOwner))
            db_manager_id.strip()
            db_manager_email = Funcionario.getMail("",db_manager_id)
            usuariostatus    = Funcionario.getUserStatus("",db_manager_id)
            
        ''' R03 - Se o owner do Banco estiver Fora - Enviar eMail para o Gestor do Mesmo'''
        if usuariostatus != "active":
            revisor=db_manager_email
        else:
            revisor = db_owner_email
 
        ''' R04 - Se qualquer atributo estiver vazio enviar email para o Administrador
                  Se nao enviar mensagem de revisao para o proprietario e para seu gestor
                  IMPORTANTE: A REVISAO E REGISTRADA EM PELO EMAIL DO ADM.
        '''
        
        Revisao.setRevisao("",db_review_id, dbName, db_owner_email, db_manager_email, dbClass)
        
        if not dbName or not dbOwner or not dbClass:
            revisor=melPropertiesFile.melStartReview_CONFIG['revisorpadrao']
            melSendMail.sendMail("",db_review_id,revisor,dbName,dbClass,"msgerr")
        else:
            melSendMail.sendMail("",db_review_id,revisor,dbName,dbClass,"msgok")
           
        ''' R05 - Uma vez concluidas as validacoes e enviado o email para o proprietario 
              egistrar a revisao no banco de dados 
        '''

    

if __name__ == "__main__":
    
    __main__()
