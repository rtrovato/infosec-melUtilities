# IMPORTANT TO CREATE A RELATIVE PATH FOR PROJECT
import sys 
sys.path.insert(0, '../mel.utils.providers')
sys.path.insert(1, '../mel.utilities')
sys.path.insert(2, '../mel.procedures')

import smtplib, ssl 

from melPropertiesFile import melSMTPProvider_CONFIG

class melSMTPProvider: 
     
    def getSMTPConnection(self):
    
        try:
            smtp_server = melSMTPProvider_CONFIG['server']
            port        = melSMTPProvider_CONFIG['port']
            sender      = melSMTPProvider_CONFIG['sender']
            passwd      = melSMTPProvider_CONFIG['passwd']
            context = ssl.create_default_context()
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender, passwd)
        
            return server
    
        except Exception as e: 
            print (str(e))

 
            
            

    

