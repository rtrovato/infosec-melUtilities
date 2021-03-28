import os
import csv 
from iamGSuiteProviders import iamGSuiteProviders
from iamUtilties import iamUtilities
import iamMassiveEmailSend

class sendMailMassive: 
    def getContatcs(path, filename): 
        listaEmail = iamUtilities.getCSVFile("",path,filename)
        return (listaEmail)

    def setMassiveMail(self):
        emailTemplatePath='/home/rtrovato/99workspace/mailMessagesTemplate'
        emailTemplateFile='iamMessageGSuiteOwners.txt'
        emailContact='iamContactsGSuiteOwners.txt'
        try:
            emailSubject = 'IMPORTANTE: SUSPENSÃO DE CONTA DE EMAIL '
            lista = iamMassiveEmailSend.sendMailMassive.getContatcs(emailTemplatePath,emailContact)
            nome=""
            for contato in lista: 
                conta = str(contato['email'])
                nome  = str(contato['nome'])
                resultado = iamUtilities.sendMail("",'conta',emailSubject,emailTemplatePath,emailTemplateFile,conta,nome)
        except Exception as e: 
            print(str(e))
            
def __main__():
    try: 
        results = sendMailMassive.setMassiveMail("")
    except Exception as e: 
        print(str(e))


if __name__ == "__main__":
    __main__()