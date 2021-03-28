import smtplib
import os 
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import httplib2
import os
from httplib2 import Http
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client import file
from exchangelib import Credentials, Account

class melGSuiteProviders: 
    ''' Hi, I am a provider to connect with GMail suite email service 
        to work with me call my principal method getGmailConnect '''
        
    def __init__ (self):
        pass 
        
    def getGmailConnect (self, component):
        try: 
            http = httplib2.Http()
            '''SCOPES = ['https://www.googleapis.com/auth/gmail.send',
                      'https://www.googleapis.com/auth/drive',
                      'https://www.googleapis.com/auth/cloud-platform',
                      'https://www.google.apis.com/auth/cloudplatformprojects.readonly'
                      ]'''


            SCOPES = ['https://www.googleapis.com/auth/gmail.send',
                      'https://www.googleapis.com/auth/drive',
                      'https://www.googleapis.com/auth/cloud-platform',
                      'https://www.googleapis.com/auth/admin.directory.group',
                      'https://www.googleapis.com/auth/admin.directory.group.member'
                      ]

            creds = None
            store = oauth2client.file.Storage('/home/rtrovato/melWorkspace/apiKeys/token.pickle')
            creds = store.get()
            if not creds or creds.invalid: 
                flow = client.flow_from_clientsecrets ('/home/rtrovato/melWorkspace/apiKeys/googleCredentials.json', SCOPES)
                flow.user_agent = "IamUtilities"
                creds = tools.run_flow(flow, store)
            if component == 'gmail' :
                service = build('gmail', 'v1', credentials=creds)
            elif component == 'driver': 
                service = build('drive','v3',credentials=creds)
            elif component == 'projetos':
                service = discovery.build('cloudresourcemanager','v1',credentials=creds)
            elif component == 'directory':
                service = build('admin','directory_v1', credentials=creds)
            return (service)  
                   
        except Exception as e: 
            print (str(e))
   
                        
    def getExchangeConnection(self): 
        usuario = input("Informe seu email completo..: ")
        senha   = input("Infome a senha por favor....: ")
        credentials = Credentials(usuario,senha)
        account = Account('ricardo.oliveira@didiglobal.com',credentials=credentials, autodiscover=True)
        
        for item in account.inbox.all().order_by('-datetime_received')[:100]:
            print(item.subject, item.sender, item.datetime_received)
