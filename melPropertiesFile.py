import os
try: 
    
    emailSender = os.environ['emailSender']
    emailPasswd = os.environ['emailPasswd']
    
except Exception as e: 
    print("Variaves emailSender e emailPasswd nao configuradas" )

melStartReviewHereJSON_CONFIG = { 
    'path':'/melDesafio/input/',
    'fileName':'databases.json'
}

melStartReviewHereCSV_CONFIG = { 
    'path':'/melDesafio/input/',
    'fileName':'proprietarios.csv'
}

melSMTPProvider_CONFIG = { 
    'server':'smtp.gmail.com',
    'port':'587',
    'sender': emailSender,
    'passwd': emailPasswd
   
}

melSendMailReview_CONFIG = { 
    'path' :'/melDesafio/input/',
    'fileName':'eMailReview.txt',
    'fileName':'Revisao de Classificacao da Informacao'
   
}

