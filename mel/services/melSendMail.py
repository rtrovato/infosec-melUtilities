# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
import mimetypes
import base64
import os
import csv 

# Bibliotecas importante para o envio de emails
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors
from string import Template


import melPropertiesFile 
from mel.providers.melSMTPProvider import melSMTPProvider



class melSendMail:
    
    def _init_(self): 
        pass
    
    def sendMail(self, to, nomebanco, classificacao, arquivo):
        messageFile     = melPropertiesFile.melSendMailReview_CONFIG['path']
        messageFile     = messageFile+melPropertiesFile.melSendMailReview_CONFIG[arquivo]
        subject         = melPropertiesFile.melSendMailReview_CONFIG['subject']
        sender          = melPropertiesFile.melSendMailReview_CONFIG['sender']
        to              = to
        nomebanco       = nomebanco
        classificacao   = classificacao
        
        
        try:
            with open (messageFile, 'r', encoding='utf-8') as csv_file: 
                csv_reader = Template(csv_file.read())
                csv_file.close()
        except Exception as e:
            print(str(e))
            
       
        try:
            service = melSMTPProvider.getSMTPConnection("")
            body = csv_reader.substitute(nomebanco=nomebanco, classificacao=classificacao)
            message = MIMEMultipart()
            message['to'] = to
            message['from'] = "Comunicado Infosec"+sender
            message['subject'] = subject
            message.attach(MIMEText(body, 'html'))
            service.sendmail(sender, to, message.as_string())
            
        except errors.HttpError as error:
            print (str(error))
            