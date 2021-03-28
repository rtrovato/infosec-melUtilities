from apiclient import errors
import os
import csv 
from iamGSuiteProviders import iamGSuiteProviders
from iamUtilties import iamUtilities
import iamMassiveEmailSend
import requests
import json

class iamGSuiteUtilities:
    
    def update_permission(service, file_id, permission_id, new_role):
        pass

    def getProjectServices(self, projectID):
        pass
        
    def listProjects (self):
        try:    
            service = iamGSuiteProviders.getGmailConnect("",'projetos')
            initialToken ="" 
            looping = True  
            contador = 0
            while looping:
                resp = service.projects().list(pageSize=150, pageToken=initialToken).execute()
                for projeto in resp.get('projects', []):
                    print(str(projeto['projectNumber']+" "+(projeto['name'])))        
                initialToken = resp.get('nextPageToken')
                if (initialToken is None):
                    looping = False
        except errors.HttpError as error:
            print (str(error))
            
    def getAnalyticsAccount (self): 
        try:
            service = iamGSuiteProviders.getGsuiteConnWithJson("")
            accounts = service.management().accounts().list().execute()
            count=0
            for item in account.get('items',[count]):
                print (str(item))
                count=count+1    
        except Exception as e: 
            print(str(e))

    def listGroupsMembers(self, grupo):
        try:
            token = ""
            lista=[]
            service = iamGSuiteProviders.getGmailConnect("","directory")
            while token is not None: 
                resp=service.members().list(groupKey=grupo, maxResults=100, pageToken=token).execute()
                if 'members' in resp:
                    lista=lista+resp['members']
                
                if 'nextPageToken' in resp:
                    token=resp['nextPageToken']
                else:
                    token=None
                    
            return(lista)
        except Exception as e:
            print(str(e()))
            
    def listGroups(self):
        try:
            token=""
            lista=[]
            service = iamGSuiteProviders.getGmailConnect("","directory")
            while token is not None:
                resp = service.groups().list(customer="my_customer",orderBy="email", maxResults=100, pageToken=token).execute()                
                if 'groups' in resp:
                    lista=lista+resp['groups']
                if 'nextPageToken' in resp:
                    token=resp['nextPageToken']
                else:
                    token=None
                    
            return(lista)
        except Exception as e:
            print(str(e()))
                    
    def printGroupsMembers (self): 
        try: 
            ''' Abre arquivo para gravacao de registros'''
            with open('grupos.csv', 'w', newline='', encoding="utf-8") as csvfile:
                csvLayout=['GrupoId','GrupoNome','GrupoeMail','TotalMembers','MemberEmail','MemberRole','MemberType']
                writer = csv.DictWriter(csvfile, fieldnames=csvLayout)
                writer.writeheader()
                '''Recupera os Grupos'''
                lista=iamGSuiteUtilities.listGroups("")                    
                ''' Lopping para cada pagina de grupos '''
                ''' Iniciar gravacao de registros de membros dos grupos'''
                for groupName in lista:
                    group        =       groupName['id']
                    grupoID      =   str(groupName['id'])
                    grupoNome    =   str(groupName['name'])
                    grupoMail    =   str(groupName['email'])
                    '''' Recuperar os membros do primeiro grupo da lista'''
                    tags = iamGSuiteUtilities.listGroupsMembers("",group)
                    ''''Se existir membros monta o looping de membros do grupo '''
                    ''' Se o grupo tiver membros entrar no looping'''
                    tagsize=len(tags)
                    
                    if tagsize > 0 :  
                        '''Looping para listar grupo e membros e escrever em arquvio'''
                        for listMember in tags: 
                            '''Se o membro nao tiver email sera ignorado'''
                            if 'email' in listMember: 
                                membereMail  =   str(listMember['email'])
                                memberRole   =   str(listMember['role'])
                                memberType   =   str(listMember['type'])
                                writer.writerow({'GrupoId' : grupoID,
                                                 'GrupoNome' : grupoNome,
                                                 'GrupoeMail' : grupoMail,
                                                 'TotalMembers' : tagsize,
                                                 'MemberEmail' : membereMail,
                                                 'MemberRole' : memberRole,
                                                 'MemberType' :  memberType
                                                })
                                    
                    else: 
                        membereMail  =  ''
                        memberRole   =  ''
                        memberType   =  ''
                        writer.writerow({'GrupoId' : grupoID,
                                                 'GrupoNome' : grupoNome,
                                                 'GrupoeMail' : grupoMail,
                                                 'TotalMembers' : tagsize,
                                                 'MemberEmail' : membereMail,
                                                 'MemberRole' : memberRole,
                                                 'MemberType' :  memberType
                                                })
                       

        except Exception as e: 
            print(str(e))

def __main__():
    try: 
        iamGSuiteUtilities.printGroupsMembers("")
    except Exception as e: 
        print (str(e))   

if __name__ == "__main__":
    __main__()