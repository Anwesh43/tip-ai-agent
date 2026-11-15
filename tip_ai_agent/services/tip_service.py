from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

load_dotenv 

class TipService:
    def __init__(self):
        headers = {
            "Authorization": f"Bearer {os.environ["TIP_API_KEY"]}"
        }
        self.client = BaseHTTPClient(os.environ["TIP_BASE_URL"], headers = headers)

    def _handleError(self, e):
        print("Error", str(e))
        return {
            "status": "Error",
            "message": str(e)
        }

    def searchProject(self, query : str):
        try:
            qpParams = {
                "q": query
            }
            response = self.client.getCall("search", qpParams = qpParams)
            keys = ["year", "name", "slug", "category", "city"]
            
            results = []
            if "results" in response:
                for res in response["results"]:
                    obj = {}
                    for key in keys:
                        obj[key] = res[key]
                    results.append(obj)
            return results 
        except Exception as e:
            return self._handleError(e)


    def getProjectDetails(self, projectSlug : str):
        try:
            response = self.client.getCall(f"project/{projectSlug}")
            return response 
        except Exception as e:
            return self._handleError(e)

    def getSimilarProjects(self, projectSlug : str):
        try:
            response = self.client.getCall(f"similar/{projectSlug}")
            return response 
        except Exception as e:
            return self._handleError(e)
    