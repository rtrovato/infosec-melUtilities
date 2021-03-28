import ldap3 
from ldap3 import Connection, Server, SUBTREE, ALL
import iamPropertiesFile
from iamActiveDirectoryProvider import iamActiveDirectoryProvider
import json
from iamUtilsProvider import iamUtilsProvider
from iamUtilties import iamUtilities

class iamActiveDirectoryAccount:
    ''' Hi worker I am a fine Class that are responsible to manager users 
        on Active Directory  server to achive this goal I have a lot of piece that I call 
        from my Hands, that are able to: 
            a. iamADSAccountSearch - Searh users on LDAP  
            b. iamADSAccountCreate - Create users on LDAP
            c. iamADSpAccountDelete - Dlete accounts on LDAP 
            d. iamADSAccountList - Recovery lists on LDAP
        To work fine I need  throught native libs also: 
            iamLdapProvider to get connect with servers 
            iamUtilsProvider to transform a lot information as fullname and login 
    ''' 

    def __init__(self, i):
        pass

    def iamADSAccountSearch(self, parametro, valor, entries):

        ''' Hi worker I am one of a lot hands from imLdapAccount, with me you are able to
                a. get true or false from a search 
                b. get entries from a search 
            for a option use y on entries parameters
        '''
        ctx = iamLdapProvider.conectar("")
        ctx.bind()
        if entries == "y":
            ctx.search('ou=people,dc=iam,dc=com,dc=br','('+parametro+'='+valor+')')
            return ctx.entries
        else: 
            return ctx.search('ou=people,dc=iam,dc=com,dc=br','('+parametro+'='+valor+')')

    def iamADSAccountCreate(self, i):
        ''' This Method is responsable to create a LDAP Account 
            its depends on iamLdapProvider to conect with server 
        '''
        emailpath='/home/rtrovato/99workspace/mailMessagesTemplate'
        emailMessage='iamMessageMobility.txt'
        try:
            ''' Read CSV File '''
            csv_to_json = iamUtilsProvider.getCSVFile("","mexicoacc.txt", "/home/rtrovato/99workspace/MexicoAccounts/")
            
            ''' Connect to Active Directory Server '''
            ctx = iamActiveDirectoryProvider.conectar("")
            
            '''Create account on Active Directory ''' 
            for row in csv_to_json: 
                nnLogin         = str(row['login'])
                nnNome          = str(row['nome'])
                nnNomeCompleto  = str(row['NomeCompleto'])
                nnPassword      = iamUtilsProvider.passwordGeneration("",12)
                nnEmail         = str(row['email'])
                ctx.add(dn='cn='+nnNomeCompleto+',OU=MX_Users,OU=Mexico,dc=didimobility,dc=local', 
                    attributes={'objectClass': ['user','person','top', 'OrganizationalPerson'],  
                                'sAMAccountName': str(nnLogin),
                                'givenName' : str(nnNome),
                                'displayName': str(nnNomeCompleto+" - "+nnLogin),
                                'mail' : str(nnEmail), 
                                'userAccountControl' : str('544'),
                                'userPrincipalName': str(nnLogin+'@didimobility.local')
                                })
                if ctx.result['result'] != 0 :
                    error = str(ctx.result['result'])
                    resultado = iamUtilities.sendMail("","ricardo.oliveira@didiglobal.com","ERROR - "+error+" - Mexico Network Account Creation",emailpath,emailMessage,nnLogin,nnPassword)
                else:
                    resultado = iamUtilities.sendMail("","ricardo.oliveira@didiglobal.com","IMPORTANT: Mexico Network Account Creation",emailpath,emailMessage,nnLogin,nnPassword)
                    try:
                       resultado =  ctx.extend.microsoft.modify_password(user,nnPassword,old_password=None, controls=None)
                       print (str(resultado))
                    except Exception as e:
                        print (str(e))
            ctx.unbind()
        except Exception as e:
            return str(e)

    def iamADSAccountDelete(self, nnAccountName):
        pass

    def iamLdapAccountList(self): 
        pass 

    def iamADSgetManager(self, parametro, valor, entries):


        ''' Hi worker I am one of a lot hands from imaADSPAccount, with me you are able to
                a. get true or false from a search 
                b. get entries from a search 
            for a option use y on entries parameters
        '''
        ctx = iamLdapProvider.conectar("")
        ctx.bind()
        if entries == "y":
            ctx.search('ou=people,dc=iam,dc=com,dc=br','('+parametro+'='+valor+')')
            print (str(ctx.response))
            return ctx.entries
        else: 
            return ctx.search('ou=people,dc=iam,dc=com,dc=br','('+parametro+'='+valor+')')


def __main__():
    try: 
        iamActiveDirectoryAccount.iamADSAccountCreate("","") 
    except Exception as e:
        print (str(e))

if __name__ == "__main__":
    __main__()