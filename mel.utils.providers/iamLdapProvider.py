import ldap3
from ldap3 import Server, Connection, SUBTREE
import ssl
import iamPropertiesFile
from iamPropertiesFile import iamLdapProvider_CONFIG

class iamLdapProvider:
    
    def __init__(self):
        pass

    def conectar(self):
        '''This Method is responsible to retur a sync connect for any ldap client 
        '''

        try:
            nnldapServer=iamPropertiesFile.iamLdapProvider_CONFIG['ldapServer']
            nnldapPort=iamPropertiesFile.iamLdapProvider_CONFIG['ldapPort']
            nnldapBindDN=iamPropertiesFile.iamLdapProvider_CONFIG['ldapBindDN']
            nnldapPassword=iamPropertiesFile.iamLdapProvider_CONFIG['ldapPassword']

            server  = ldap3.Server(nnldapServer, nnldapPort, use_ssl=False, get_info='ALL')
            ctx     = ldap3.Connection(server, nnldapBindDN, nnldapPassword)

            return ctx

        except Exception as e:
            print ("Falha ao se autenticar no servidor" + str(e))


        '''Create server connection & return to client 
        '''

def __main__():
    pass
if __name__ == "__main__":
    __main__()
    
   
    

