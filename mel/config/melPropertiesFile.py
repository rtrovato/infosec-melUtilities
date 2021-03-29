import os
try: 
    
    emailSender     = os.environ['emailSender']
    emailPasswd     = os.environ['emailPasswd']
    mysqlAccount    = os.environ['mysqlAccount']
    mysqlPasswd     = os.environ['mysqlPasswd']
    
except Exception as e: 
    print("Variaves emailSender e emailPasswd nao configuradas" )

melStartReview_CONFIG = { 
    'revisorpadrao':'ricardo.trovato@gmail.com'
}

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
    'msgok':'melMessageReview.html',
    'msgerr':'melMessageErro.html',
    'subject':'Revisao de Classificacao da Informacao',
    'sender' : emailSender
   
}

melMYSQLConn_CONFIG = { 
    'server':'127.0.0.1',
    'port':'3306',
    'mysqlAccount': mysqlAccount,
    'mysqlPasswd': mysqlPasswd,
    'mysqlDatabase':'melproject'
   
}

