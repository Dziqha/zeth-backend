from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, Header, Path, Request
from fastapi.responses import JSONResponse

from ..configs.hash import hash_password, verify_password
from ..middlewares.auth import require_auth
from ..services.authentication.user_auth_service import User

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str
    profile_image: str

class UserChangePassword(BaseModel):
    old_password: str
    new_password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdateProfile(BaseModel):
    name: str
    username: str

class UserRequestEmail(BaseModel):
    email: str

class ResetPassword(BaseModel):
    password: str

class ProfilePicture(BaseModel):
    image: str

@router.post("/auth/register")
def add_user(user: UserCreate):
    try:
        user = User(name= user.name, username=user.username, password=hash_password(user.password), email=user.email, profile_image=user.profile_image)
        response = user.signup()
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/auth/login")
def login(userLogin: UserLogin):
    try:
        user = User()
        response = user.login(email=userLogin.email, password=userLogin.password)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/auth/update-profile")
@require_auth
async def update_user(request: Request, update_data: UserUpdateProfile):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        user = User(user_id=user_id, name=update_data.name, username=update_data.username)

        response = user.updateProfile()
        
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/auth/change-password")
@require_auth
async def update_user(request: Request, password: UserChangePassword):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        user = User(user_id=user_id)
        response = user.change_password(password.old_password, password.new_password)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/auth/profile")
@require_auth
async def get_profile(request: Request):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        user = User()
        response = user.get_by_id(user_id)
        
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
    
        result = response["data"]

        filtered_response = {
            "status": response["status"],
            "data": {
                "user_id": session["user_id"],
                "name": result.get("name"),
                "username": result.get("username", "N/A"),
                "email": result.get("email", "N/A"),
                "profile_picture": result.get("profile_image", "N/A"),
            }
        }
        
        return JSONResponse(filtered_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/auth/verify")
async def request_verify_email(userData: UserRequestEmail):
    try:
        user = User(email=userData.email)

        response = user.handle_request_verify_email()

        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/auth/verify/{token}')
async def verify_email(token: str = Path(...)):
    try:
        user = User()
        response = user.handle_verify_email(token=token)

        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/auth/reset-password")
async def request_reset_password_email(userData: UserRequestEmail):
    try:
        user = User(email=userData.email)

        response = user.handle_request_reset_password_email()

        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/auth/reset-password/{token}')
async def reset_password(password: ResetPassword, token: str = Path(...)):
    try:
        user = User(password=password.password)
        response = user.handle_reset_password(token=token)

        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/auth/profile-picture")
@require_auth
async def add_user(request: Request, image: ProfilePicture):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")
                
        user = User(user_id=user_id)
        response = await user.upload_profile_picture(image=image.image)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))