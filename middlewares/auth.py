import os, jwt
from functools import wraps
from fastapi import Request, HTTPException
from typing import Callable

from dotenv import load_dotenv

load_dotenv()

def require_auth(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = None
        for arg in args:
            if isinstance(arg, Request):
                request = arg
                break
        if not request:
            request = kwargs.get('request')
        
        if not request:
            raise HTTPException(status_code=500, detail="Request object not found")

        authorization = request.headers.get("Authorization")

        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid or missing token")
            
        token = authorization.split("Bearer ")[1]
        
        try:
            session_data = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=['HS256'])
            request.state.session = session_data 
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return await func(*args, **kwargs)
    
    return wrapper
