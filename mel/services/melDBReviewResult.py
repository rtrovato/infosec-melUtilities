import os 
from mel.providers.melMySQLProvider import melMySQLProvider

class melDBReviewResult: 
    def _init_(self):
        pass
    
    def getUltimaRevisao(self):
        ''' Metodo utilizado para recuperar o ultimo registro de reivsao e assim disponibilizar o proximo numero
        ''' 
        try: 
            selecionar = "select coalesce(max(id),0) + 1 from mel_review_result"
            ctx = melMySQLProvider.getMySQLConnection("")
            cur=ctx.cursor()
            cur.execute(selecionar)
            results = cur.fetchall()
            return results
        except Exception as e: 
            print (str(e))
    
    def setReviewResult(self, db_review_id, db_data_review, dbname, db_owner_mail, db_manager_mail, db_classificacao):
        
        try:
            insert = "insert into mel_review_result (id, create_time, name_db, email_owner_db, email_owner_manager, classification_db) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (db_review_id, db_data_review, dbname, db_owner_mail, db_manager_mail, db_classificacao) 
            
            ctx = melMySQLProvider.getMySQLConnection("")
            cur=ctx.cursor()
            cur.execute(insert, valores)
            results = ctx.commit()
            return results
            
        except Exception as e: 
            print (str(e))

if __name__ == "__main__":
    passs
    
    
    