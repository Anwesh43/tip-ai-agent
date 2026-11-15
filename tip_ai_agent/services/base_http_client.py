import requests 
from typing import Dict 
from urllib.parse import urlencode 

class BaseHTTPClient:
    def __init__(self, baseURL : str, headers : Dict):
        self.baseURL = baseURL 
        self.headers = headers 

    def getCall(self, endpoint : str, qpParams : Dict = {}):
        response = requests.get(f"{self.baseURL}/{endpoint}?{urlencode(qpParams)}", headers = self.headers)
        response.raise_for_status()
        return response.json()
