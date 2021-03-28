
# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
sys.path.insert(0, '../mel.utils.providers')
sys.path.insert(1, '../mel.utilities')
sys.path.insert(2, '../mel.procedures')

#STARTED PROGRAM HERE
import os
import json
from mel


''' Hi I m the Review Database Orquestrator when I am wokring   I do: 
    1. Create Database collection from json and to be reviewd 
        a. I Need melDatabaseObj to create melDatabase Class  
    2. After received users from step 1  I request to my friends :

   
    '''

def __main__(): 
    try: 
        getNewUsers() 
    except Exception as e:
        print (str(e))

def getNewUsers(): 

    nnNewPerson = iamHumanResourcesPerson.getListEmployee('','funcionarios','obterAdmitidos','anoMes','201701')
    
    for i in (nnNewPerson):
        tmpUser = i
        if iamUtilsProvider.getNullAttribute('',tmpUser) : 
            raise Exception ("Registro nao processo devido a valores nulos ")

        userExist = iamLdapAccount.iamLdapAccount.iamLdapAccountSearch('','nnEmployeeNumber',i['Registro'],'n')
        if userExist :
            pass 
        else: 
            addLdapResult = iamLdapAccount.iamLdapAccount.iamLdapAccountCreate('',tmpUser)
            print (addLdapResult)

if __name__ == "__main__":
    __main__()
