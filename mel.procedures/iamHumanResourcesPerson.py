import sys
import json
import iamActiveDirectoryAccount
import iamGSuiteAccount
import iamOrisPortalProvider
from   iamOrisPortalProvider import iamOrisProvider
from unicodedata import normalize

''' 
    Hi dear I am iamHumanResourcesPerson, I am a class guy and like so much to interact with :
        1. iamOrisPortalProvider , that provider for me information about 99 FTS allways that 
        a friend request some information from them
   
    It is very important for you to know that I not work alone, if you need some information from me
    you need to know pieces of my body that are: 
        1. getListEmployee
        2. getSingleEmployee
        3. getTerminatedEmployeeList 
'''
           
 
class iamHumanResourcesPerson:

    def __init__(self):
        pass

        ''' This function has as the mainly obejctive to read all news FTES. 
            and call the accounts
        '''

    def getListEmployee(self, classe, metodo, parametro, filtro):
        ''' Hi man/girl how are you ? I am one of a lot iamHumanResourcesPerson hands 
            If you need I can offers a LIST of Employee on a json payload that contain a 
            lot of information from them, to CALL ME you need to inform : 
            classe : I meant, what kind of employee actual Oris has only "funcionarios" 
            metodo : I meant, what action you want to perfom, example obterAdmitidos 
                     to know more about metodo please look orion documentation
            parametro : For each metodo you can have a diferent parametro, a examplo is "anoMes"
            filtro : It is a operator like = > < =!
        '''

        url = iamPropertiesFile.iamOrisPortalProvider_CONFIG['url']
        strclasse = classe
        strmetodo = metodo
        strparm   = parametro 
        strvalor  = str(filtro) 
        objeto    = iamOrisProvider.iamOrisConnection("", url, strclasse, strmetodo, strparm, strvalor)
        
        return objeto

    def getSingleEmployee(self, classe, metodo, parametro, filtro):

        ''' Hi man/girl how are you ? I am one of a lot iamHumanResourcesPerson hands 
            If you need I can offers a SINGLE Employee on a json payload that contain a 
            lot of information from her/him, to CALL ME you need to inform : 
            classe : I meant, what kind of employee actual Oris has only "funcionarios" 
            metodo : I meant, what action you want to perfom, example obterAdmitidos 
                     to know more about metodo please look orion documentation
            parametro : For each metodo you can have a diferent parametro, a examplo is "id"
            filtro : It is a operator like = > < =!
        '''
        url = iamPropertiesFile.iamOrisPortalProvider_CONFIG['url']
        strclasse = classe
        strmetodo = metodo
        strparm   = parametro 
        strvalor  = str(filtro) 

        return iamOrisProvider.iamOrisConnection("", url, strclasse, strmetodo, strparm, strvalor)

    def getTerminatedEmployeeList(self, classe, metodo, parametro, filtro):
        ''' This Method return a json with a Terminated List Employees based on year 
            and month filter 
            Parameters:(self, parametro, filtro)
        '''
        url = iamPropertiesFile.iamOrisPortalProvider_CONFIG['url']
        strclasse = classe
        strmetodo = metodo
        strparm   = parametro 
        strvalor  = str(filtro)
        return iamOrisProvider.iamOrisConnection("", url, strclasse, strmetodo, strparm, strvalor)

    def getTerminatedEmployee(self, classe, metodo, parametro, filtro):
        strurl = iamPropertiesFile.iamOrisPortalProvider_CONFIG['url']
        strclasse = iamPropertiesFile.iamOrisPortalProvider_CONFIG['classe']
        strmetodo = iamPropertiesFile.iamOrisPortalProvider_CONFIG['metodo']
        strparm = parametro 
        strvalor = str(filtro)
        return iamOrisProvider.iamOrisConnection("", strurl, strclasse, strmetodo, strparm, strvalor)
    


  