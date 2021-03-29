import os 
from mel.providers.melMySQLProvider import melMySQLProvider

class melDBFuncionarios: 
    def _init_(self):
        pass
    
    def getFuncionario(self, user_id):
        try: 
            selecionar = "select * from mel_funcionarios where user_id="+str(user_id);
            ctx = melMySQLProvider.getMySQLConnection("")
            cur=ctx.cursor()
            cur.execute(selecionar)
            results = cur.fetchall()
            
            return results
            
        except Exception as e: 
            print (str(e))

if __name__ == "__main__":

    
    