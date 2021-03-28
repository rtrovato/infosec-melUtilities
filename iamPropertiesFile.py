# This file is conventioned to be a property file to iamoverhaul 
# automated procedures
import os
try:

    password = os.environ['iamOrisPassword']
    passwordGitToken = os.environ['iamOrisPassword']
    adsPassword = os.environ['iamADSPassword']

except Exception as e: 
    print("Variavel de senha nao configurada !!!")

iamGitHubProvider_CONFIG = { 
    'tokenInfo' : passwordGitToken,
    'url' : 'https://api.github.com/',
    'org99' : '99Taxis',
    'listOrgRepos' : 'org/99Taxis/repos'
}
''' Configuration for LDAP Connections ''' 

iamLdapProvider_CONFIG = {
    'ldapServer' : 'localhost',
    'ldapPort' : 389,
    'ldapBaseDN': 'dc=iam,dc=com,dc=br',
    'ldapBindDN' : 'cn=Administrator,dc=iam,dc=com,dc=br',
    'ldapPassword' : 'Senhas@123'
}


''' Configuration for LDAP Connections ''' 

iamActiveDirectoryProvider_CONFIG = {
    'adspServer' : '172.18.129.200',
    'adspPort' : 636,
    'adspBaseDN' : 'dc=didimobility,dc=local',
    'adspBindDN' : 'cn=Ricardo Oliveira Trovato - ADM,ou=ADM,ou=Services,dc=didimobility,dc=local',
    'adspPassword' : adsPassword
}
''' Configuration to iamHumanResourcesPerson - Calculate Login '''

iamHumanResourcesPersonCalculateLogin_CONFIG = { 
    'first_rule'   : 'nnFirstName[]'+'.'+'nnLastName[]',
    'second_rule'  : 'nnFirstName[1,1]'+'.'+'nnLastName[]',
    'third_rule'   : 'nnLastName[]'+'.'+'nnFirstName[]',
    'fourth_rule'  : 'nnLastName[1,1]'+'.'+'nnFirstName[]'
}

iamOrisPortalProvider_CONFIG = { 
    'headers'   : {'Content-type': 'application/json', 'Content-encoding': 'gzip'},
    'user'      : '212',
    'password'  :  password,
    'url'       : 'https://portal.orisrh.com:9878/apiV1/json/',
    'classe'    : 'funcionarios',
    'metodo'    : 'obterAdmitidos',
    'parametro' : 'anoMes',
    'valor'     : '201901',
}

