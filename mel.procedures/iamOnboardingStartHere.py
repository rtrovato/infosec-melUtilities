from iamHumanResourcesPerson import iamHumanResourcesPerson 
from iamLdapAccount import iamLdapAccount
import os
import iamLdapAccount
import json
from iamUtilsProvider import iamUtilsProvider

''' Hi I m the IAM Onboarding Orquestrator when I work I do: 
    1. Get new users from ORis - iamHumaResourcesPerson
    2. After received users from step 1  I request to my friends :
        a. iamLdapAccount 
        b. iam GSuiteAccount 
        c. iamActiveDirectory 
    
    to create the new account from our 99ners employees. 
    
    3. If everything is fine I register a log on my friend MySQL request help to iamutilsProvider.

    If you need me please type on commandline py iamOnboardingStartHere <action> that can be: 
        a. onboardingUsers
        b. offboardingUsers
        c. updateUsers
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
