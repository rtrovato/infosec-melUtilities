import os 
from mel.providers.melMySQLProvider import melMySQLProvider

class melDBReviewResult: 
    def _init_(self):
        pass
    
    def setReviewResult(self):
        try: 
            insert = "insert into mel_review_result (create_time, name_db, email_owner_db, email_owner_manager, classification_db) VALUES (%s, %s, %s, %s, %s)"
            valores = ('2020-01-01', 'dbname', 'ricardo@gmail.com', 'matilde@gmail.com', 'CONFIDENCIAL') 
                            
            ctx = melMySQLProvider.getMySQLConnection("")
            cur=ctx.cursor()
            cur.execute(insert, valores)
            results = ctx.commit()
            return results
            
        except Exception as e: 
            print (str(e))

if __name__ == "__main__":
    obj = melDBReviewResult.setReviewResult("")
    print (str(obj));
    
    
    
    