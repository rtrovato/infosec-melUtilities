from apiclient import errors
import os
import csv 
from iamGSuiteProviders import iamMailProviders
from iamUtilties import iamUtilities
import iamMassiveEmailSend

class iamGsuiteProjects:
    
    def update_permission(service, file_id, permission_id, new_role):
        """Update a permission's role.

        Args:
            service: Drive API service instance.
        file_id: ID of the file to update permission for.
        permission_id: ID of the permission to update.
        new_role: The value 'owner', 'writer' or 'reader'.
        Returns:
        """
        
    def getProjectServices(self, projectID):

        service = "texto"
        
        
    def listProjects (self):
        try:    
            service = iamMailProviders.getGmailConnect("",'projetos')
            initialToken ="" 
            looping = True  
            contador = 0
            while looping: 
                request = service.projects().list(pageSize=150, pageToken=initialToken).execute()
                for projeto in request.get('projects', []):
                    servico = iamGsuiteProjects.getProjectServices("")
                    print(str(servico))         
                    
                initialToken = request.get('nextPageToken')
                if (initialToken is None):
                    looping = False
                
        except errors.HttpError as error:
            print (str(error))
  
def __main__():
    try: 
        results = iamGsuiteProjects.listProjects("")
        
    except Exception as e: 
        print(str(e))

if __name__ == "__main__":
    __main__()