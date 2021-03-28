
import os 
import ssl
import melPropertiesFile

import mysql.connector

class melMySQLProvider: 
    def _init_():
        pass
    
    def getMySQLConnection(self):
        mysqlServer     = melPropertiesFile.melMYSQLConn_CONFIG['server']
        mysqlAccount    = melPropertiesFile.melMYSQLConn_CONFIG['mysqlAccount']
        mysqlPasswd     = melPropertiesFile.melMYSQLConn_CONFIG['mysqlPasswd']
        mysqlDataBase   = melPropertiesFile.melMYSQLConn_CONFIG['mysqlDatabase']
        
        try: 
            db_connection = mysql.connector.connect(host=mysqlServer,\
                                                    user=mysqlAccount,\
                                                    passwd=mysqlPasswd,\
                                                    database=mysqlDataBase)
            cursor = db_connection.cursor()
            return cursor
        
        except Exception as e: 
            print (str(e))
            
if __name__ == "__main__":
    ctx = melMySQLProvider.getMySQLConnection("")



