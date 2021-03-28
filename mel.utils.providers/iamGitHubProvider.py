import sys
import json
import os
import http.client
import urllib3
import requests 
from requests.auth import HTTPBasicAuth
import base64 
import iamPropertiesFile

class iamGitHubProvider:
        ''' The iamOrisProvider is responsible to return a security connection for any 
            IAM Oris Client. 
            Parameters (url, classe, metodo, parametro, valor)
        '''

        def __init__(self):
                pass

        def iamGitConnection(self,url,action):
                try: 
                        headers = {'Content-type': 'application/json; charset=UTF-8', 
                                   'Content-encoding': 'gzip',
                                   'VERSION': '2',
                                   'Accept': 'application/vnd.github.v3+json',
                                   'Authorization' : 'Token '+ iamPropertiesFile.iamGitHubProvider_CONFIG['tokenInfo'],
                                   }
                        url = url
                        action = action
                        requisicao=url+action
                        resp = requests.get(requisicao, headers=headers)
                        retorno = resp.status_code
                        if retorno == 200 :
                                return resp.json()
                        else :
                                return resp.status_code                        
                except Exception as e:
                        return str(e)
                 
def __main__() :
        c = 0
        continuar= 'true'
        retorno = 'x' 
        while continuar == "true" :
                retorno = iamGitHubProvider.iamGitConnection('','https://api.github.com/','users?since='+str(c)+'&per_page=100')
                if len(retorno) >=0 :
                        c=c+len(retorno)+1
                for m in retorno :
                        login=m['login']
                        nome =str(m['id'])
                        '''rmail=iamGitHubProvider.iamGitConnection('','https://api.github.com/','users/'+login)
                        email=str(rmail['email'])
                        '''
                        email=str("meu@nosso.com")
                        siteadmin = str(m['site_admin'])
                        registro = str(c)
                        AtributeValue=(login+','+nome+','+email+','+siteadmin + ',' + registro + ' , '+email)
                        print (str(AtributeValue))


if __name__ == "__main__":
    __main__()

    