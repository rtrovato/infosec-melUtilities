import ldap3 
from ldap3 import Connection, Server, SUBTREE, ALL
import iamPropertiesFile
from iamLdapProvider import iamLdapProvider
from iamHumanResourcesPerson import iamHumanResourcesPerson
import json
import iamUtilsProvider


class iamLdapAccount:
    ''' Hi worker I am a fine Class that are responsible to manager users 
        on ldap server to achive this goal I have a lot of piece that I call 
        from my Hands, that are able to: 
            a. iamLdapAccountSearch - Searh users on LDAP  
            b. iamLdapAccountCreate - Create users on LDAP
            c. iamLdapAccountDelete - Delete accounts on LDAP 
            d. iamLdapAccountList - Recovery lists on LDAP
        To work fine I need  throught native libs also: 
            iamLdapProvider to get connect with servers 
            iamUtilsProvider to transform a lot information as fullname and login 

    ''' 

    def __init__(self, i):
        try : 
            self.nnNome                = iamUtilsProvider.iamUtilsProvider.fullNameSeparation("",i['Nome']).upper()
            self.password               = iamUtilsProvider.iamUtilsProvider.passwordGeneration("")
            self.nnRegistro             = i['Registro']
            self.nnLogin                = iamUtilsProvider.iamUtilsProvider.loginCalc('',self.nnNome).lower()

            if self.nnLogin == 'null' : 
                raise Exception("Registro | " + self.nnRegistro + "Nao cadastrado proceder manualmente")
                
            self.nnDataAdmissao         = i['Admissao']
            self.nnEmail                = i['Email']
            self.nnCategoria            = 'FTE'
            self.nnCelular              = i['TelefoneCelular']
            self.nnSituacaoRH           = i['Situacao']
            self.nnCargo                = i['Cargo']
            self.nnLotacao              = i['Lotacao']
            self.nnCentroCusto          = i['CentroCusto']
            self.nnRegistroResonsavel   = i['RegistroResponsavel']
            self.nnNomeResponsavel      = i['NomeResponsavel']
            self.nnLoginResponsavel     = iamLdapAccount.iamLdapgetManager('','nnEmployeeNumber',i['RegistroResponsavel'],'y')
        except Exception as e: 
            print (str(e))
      
    def iamLdapAccountSearch(self, parametro, valor, entries):

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

    def iamLdapAccountCreate(self, i):
        ''' This Method is responsable to create a LDAP Account 
            its depends on iamLdapProvider to conect with server 
        '''

        newiamLdapAccount = iamLdapAccount(i)
        try:
            print ("Tentando" + newiamLdapAccount.nnLogin)
            ctx = iamLdapProvider.conectar("")
            ctx.bind()
            ctx.add(dn='cn='+newiamLdapAccount.nnLogin+',ou=people,dc=iam,dc=com,dc=br', 
                    attributes={'objectClass': ['nineninesPerson','top'],  
                                'uid': str(newiamLdapAccount.nnLogin),
                                'nnFullName' : str(newiamLdapAccount.nnNome),
                                'nnEmployeeNumber': str(newiamLdapAccount.nnRegistro),
                                'nnMail': str(newiamLdapAccount.nnEmail),
                                'nnCategory' : str(newiamLdapAccount.nnCategoria),
                                'nnMobileNumber' : str(newiamLdapAccount.nnCelular),
                                'nnTitle' : str(newiamLdapAccount.nnCargo),
                                'nnDepartmentNumber' : str(newiamLdapAccount.nnLotacao),
                                'nnLastName' : 'Lastname',
                                'nnManagerName' : str(newiamLdapAccount.nnLoginResponsavel)
                                })
            if ctx.result['result'] != 0 :
                error = str(ctx.result['result'])
                return error
            else:
                return ("Sucesso na Criacao" + str(newiamLdapAccount.nnLogin))
        except Exception as e:
            return str(e)

    def iamLdapAccountDelete(self, nnAccountName):
        pass

    def iamLdapAccountList(self): 
        pass 

    def iamLdapgetManager(self, parametro, valor, entries):

        ''' Hi worker I am one of a lot hands from imLdapAccount, with me you are able to
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

if __name__ == "__main__":
    pass
        