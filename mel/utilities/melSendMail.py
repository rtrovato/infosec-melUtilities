# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
sys.path.insert(0, '../mel.utils.providers')
sys.path.insert(1, '../mel.utilities')
sys.path.insert(2, '../mel.procedures')

import mimetypes
import base64
import os
from apiclient import errors

from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import melPropertiesFile 
from melSMTPProvider import melSMTPProvider


class melSendMail:
    
    def _init_(self): 
        pass
    
    def sendMail(self, manager):
        messageFile = melPropertiesFile.melSendMailReview_CONFIG['path']
        messageFile = messageFile+melPropertiesFile.melSendMailReview_CONFIG['eMailReview.txt']
        subject     = melPropertiesFile.melSendMailReview_CONFIG['subject']
        sender =  os.environ['sender']
        to =  "ricardo.trovato@gmail.com"
        try:
            with open (messageFile, 'r', encoding='utf-8') as csv_file: 
                csv_reader = Template(csv_file.read())
                csv_file.close()
        except Exception as e:
            print(str(e))
            
            
        service = melSMTPProvider.getSMTPConnection()
        
        body = csv_reader.substitute(nomebanco="CARTAO", classificacao="CONFIDENCIAL")
        try:
            message = MIMEMultipart()
            message['to'] = to
            message['from'] = "Comunicado Infosec"+os.environ['sender']
            message['subject'] = subject
            message.attach(MIMEText(body, 'html'))
            mensagem ={'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('utf-8')}
            resultado = (service.users().messages().send(sender=sender, body=mensagem).execute())
            del message
        except errors.HttpError as error:
            print (str(error))
            
if __name__ == "__main__":
    melSendMail.sendMail("","Ricardo Trovato")
    
    