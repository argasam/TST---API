from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            url = "http://128.199.106.160/arga/validate"
            headers = {
                "accept": "application/json",
                "Authorization" : f"Bearer {credentials.credentials}"
            }
            response = requests.post(url, headers=headers)
            return response.json()
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")