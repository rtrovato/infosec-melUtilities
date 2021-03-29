import os 
from mel.providers.melMySQLProvider import melMySQLProvider

class melDBFuncionarios: 
    def _init_(self):
        pass
    def getFuncionario(self):
        try: 
            selecionar = "select * from mel_funcionarios"
            ctx = melMySQLProvider.getMySQLConnection("")
            cur=ctx.cursor()
            cur.execute(selecionar)
            results = cur.fetchall()
            
            return results
            
        except Exception as e: 
            print (str(e))

if __name__ == "__main__":
    obj = melDBFuncionarios.getFuncionario ("")
    for i in obj:
        print (str(i))
    
    
    