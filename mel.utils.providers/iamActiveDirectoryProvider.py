import ldap3
from ldap3 import Server, Connection, SUBTREE
import ssl
import socket
import iamPropertiesFile
from iamPropertiesFile import iamActiveDirectoryProvider_CONFIG

class iamActiveDirectoryProvider:
    
    def __init__(self):
        pass

    def conectar(self):
        '''This Method is responsible to retur a sync connect for any ldap client 
        '''

        try:
            adsServer   = iamActiveDirectoryProvider_CONFIG['adspServer']
            adsPort     = iamActiveDirectoryProvider_CONFIG['adspPort']
            adsBindDN   = iamActiveDirectoryProvider_CONFIG['adspBindDN']
            adsPassword = iamActiveDirectoryProvider_CONFIG['adspPassword']

            '''tls_configuration = Tls(ssl.CERT_REQUIRED, version=ssl.PROTOCOL_SSLv3)'''
            server  = ldap3.Server(adsServer, adsPort, use_ssl=True, get_info='ALL')
            ctx     = ldap3.Connection(server, adsBindDN, adsPassword)
            ctx.start_tls
            ctx.open()
            ctx.bind()
            return ctx

        except Exception as e:
            print ("Falha ao se autenticar no servidor" + str(e))


        '''Create server connection & return to client 
        '''

def __main__():
    pass
if __name__ == "__main__":
    __main__()
    
   
    

