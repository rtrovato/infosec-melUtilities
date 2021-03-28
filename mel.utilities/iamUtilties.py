import sys
import logging
import logging.handlers 
import collections
import string
import json
import csv
import random
import os.path
from iamGSuiteProviders import iamGSuiteProviders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import base64
from apiclient import errors
from string import Template


preposicao = ['Da','da','Das','das','DA','DAS','DO','DOS','Do','do','Dos','dos',
               'De','de','Des','des','DE','DES','junior','Juniors','JUNIORS',
               'FILHO','filho','FILHOS', 'NETO', 'Neto', 'neto', 'Jr.', 'JR']

class iamUtilities:

    def removerAcentos(self, txt):
        table = collections.defaultdict(lambda: None)
        table.update({
        ord('à'):'a', ord('á'):'a', ord('â'):'a', ord('ä'):'a', ord('ã'):'a', 
        ord('è'):'e', ord('é'):'e', ord('ê'):'e', ord('î'):'i', ord('ô'):'o',
        ord('ò'):'o', ord('ó'):'o', ord('ō'):'o', ord('õ'):'o', ord('û'):'u',
        ord('ü'):'u', ord('ù'):'u', ord('ú'):'u', ord('ū'):'u', ord('ç'):'c',
        ord('ć'):'c', ord('č'):'c', ord(' '):' ', ord('\N{NO-BREAK SPACE}'): ' ',
        ord('\N{EN SPACE}'): ' ', ord('\N{EM SPACE}'): ' ', ord('\N{THREE-PER-EM SPACE}'): ' ',
        ord('\N{FOUR-PER-EM SPACE}'): ' ', ord('\N{SIX-PER-EM SPACE}'): ' ',
        ord('\N{FIGURE SPACE}'): ' ', ord('\N{PUNCTUATION SPACE}'): ' ',
        ord('\N{THIN SPACE}'): ' ', ord('\N{HAIR SPACE}'): ' ', ord('\N{ZERO WIDTH SPACE}'): ' ',
        ord('\N{NARROW NO-BREAK SPACE}'): ' ', ord('\N{MEDIUM MATHEMATICAL SPACE}'): ' ',
        ord('\N{IDEOGRAPHIC SPACE}'): ' ', ord('\N{IDEOGRAPHIC HALF FILL SPACE}'): ' ',
        ord('\N{ZERO WIDTH NO-BREAK SPACE}'): ' ', ord('\N{TAG SPACE}'): ' ', })

        table.update(dict(zip(map(ord,string.ascii_uppercase), string.ascii_lowercase)))
        table.update(dict(zip(map(ord,string.ascii_lowercase), string.ascii_lowercase)))
        table.update(dict(zip(map(ord,string.digits), string.digits)))

        txt = txt.translate(table,)
        return txt

    def loginCalc(self, i):
        fullName = str(i)
        x = fullName.split()
        n = len(x)
        for i in range(len(x)):
            n = n - 1
            loginToSearch=x[0]+'.'+x[n]
            if n <= 0 :
                return 'null'
            else: 
                if iamLdapAccount.iamLdapAccount.iamLdapAccountSearch('','uid', str(loginToSearch),'n') :
                    pass
                else: 
                    return str(loginToSearch)

    def fullNameSeparation(self, i):
        fullName = ''
        tmpFullName = iamUtilsProvider.removerAcentos('',str(i))
        nameToTest = tmpFullName.split()
        for n in (nameToTest):
            if n.upper() in artigos:
                n = ''
            else: 
                fullName = fullName+' '+str(n)
                fullName = fullName.capitalize()        
        return str(fullName)
    
    def passwordGeneration(self, tamanho):
            caracter=['maiusculas','minusculas','numeros','especiais']
            maiusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
            minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
            numeros=["1","2","3","4","5","6","7","8","9","0"]
            especiais=["!","@","#","$","^","&","*"]
            password=""
            selecionar=""
            selecionado=""
            for i in range(tamanho):
                while selecionar == selecionado: 
                    selecionar = random.choice(caracter)
                if selecionar == "maiusculas" : password = password+random.choice(maiusculas)
                if selecionar == "minusculas" : password = password+random.choice(minusculas)
                if selecionar == "numeros"    : password = password+random.choice(numeros)
                if selecionar == "especiais"  : password = password+random.choice(especiais)
                selecionado = selecionar
            return password

    def getNullAttribute(self,i) :
        ''' Hi I am responsible to check if some attribute on json object is null 
            if yes I will raise a exception 
             
        '''
        j = i
        print (str(j))
        valores = json.loads(j)
        for person in j :
            AtributeValue=valores['CidadeResidencia']
            print (str(AtributeValue))
            
    def sendLog(self, level, detail):
        try:
            nivel = str(level)
            nivel = nivel.upper()
            LoggerEvent = logging.getLogger("logToSend")
            if nivel == 'INFO' : LoggerEvent.setLevel(logging.INFO)
            if nivel == 'WARN' : LoggerEvent.setLevel(logging.WARN)
            if nivel == 'DEBUG' : LoggerEvent.setLevel(logging.DEBUG)
            LoggerHandler = logging.handlers.SysLogHandler('localhost',514)
            LoggerEvent.addHandler(LoggerHandler)
            LoggerEvent.INFO(detail)
        except Exception as e: 
            print(e)

    def sendMail(self, to, subject, pathTemplate, messageTemplate, login, password):
        '''To call this method you need give me the follow parameters 
            to - Who will received your message 
            subject - Please give me a beautyful Title for the message 
            messageTemplate - The message template name
            pathTemplate - The path where I can found the messageTemplate
        '''
        ''' First let me open the message file '''
        file = pathTemplate+"/"+messageTemplate
        try:
            with open (pathTemplate+"/"+messageTemplate, 'r', encoding='utf-8') as csv_file: 
                csv_reader = Template(csv_file.read())
                csv_file.close()

        except Exception as e:
            print(str(e))

        ''' Now I will connect to Gmail Server using a owner client id '''

        service = iamSendMailProvider.getGmailConnect("")
        resultado=""

        ''' Lets try send the email ''' 
        corpo = csv_reader.substitute(login=login, password=password)
        try:
            message = MIMEMultipart()
            message['to'] = to
            message['from'] = "Comunicado Infosec<noreply@99app.com>"
            message['subject'] = subject
            message.attach(MIMEText(corpo, 'html'))
            mensagem ={'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('utf-8')}
            resultado = (service.users().messages().send(userId='noreply@99app.com', body=mensagem).execute())
            del message
        except errors.HttpError as error:
            print (str(error))

    def getCSVFile(self, filePath, fileName):
        with open (filePath+'/'+fileName) as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',')
            objeto = list()
            for row in csv_reader: 
                objeto.append(row)
            dados = [dict(zip(objeto[0],row)) for row in objeto]
            dados.pop(0)            
            return dados