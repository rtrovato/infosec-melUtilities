import os 
from mel.providers.melMySQLProvider import melMySQLProvider

class melDBFuncionarios: 
    def _init_(self):
        pass
    def getFuncionario(self):
        try: 
            ctx = melMySQLProvider.getMySQLConnection("")
            selecionar = "SELECT * FROM mel_funcionarios"
            ctx.execute(selecionar)
        except Exception as e: 
            print (str(e))

if __name__ == "__main__":
    obj = melDBFuncionarios.getFuncionario ("")
    
    
    