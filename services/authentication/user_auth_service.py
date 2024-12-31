import os, aiohttp, base64
from bson import ObjectId
import jwt
from datetime import datetime, timedelta
from typing import  Dict, Union, Any
from .auth_model_service import Auth
from ...configs.database import db_instance as db
from ...configs.hash import hash_password, verify_password
from dotenv import load_dotenv

from ..interface.mail_interface_service import (
    ActivationNotification,
    ResetPasswordNotification,
) 

load_dotenv()
class User(Auth):
    def __init__(self, user_id: str = None, name: str ='', username: str = '', password: str = '', email: str = '', profile_image: str = None):
        self.user_id = user_id 
        self.name = name
        self.username = username
        self.email = email
        self.profile_image = profile_image
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.collection = db.get_collection('users') 

    def signup(self) -> Dict[str, Union[str, Any]]:
        try:
            if self.collection.find_one({"email": self.email}):
                return {
                    "status": 400,
                    "message": "Email already registered"
                }
            if self.collection.find_one({"username": self.username}):
                return {
                    "status": 400,
                    "message": "Username already in use"
                }
            user_data = {
                "name": self.name,
                "username": self.username,
                "email": self.email,
                "password": self.password,
                "profile_image": self.profile_image,
                "created_at": self.created_at
            }
            result = self.collection.insert_one(user_data)
            if result.inserted_id:
                return {
                    "status": 201,
                    "message": f"User '{self.username}' created successfully."
                }
            else:
                return {
                    "status": 400,
                    "message": "Failed create user"
                }
        except:
            return {"status": 500, "message": "Internal server error"}

    def get_by_id(self, user_id: int) -> Dict[str, Union[str, Any]]:
        try:
            user = self.collection.find_one({"_id": ObjectId(user_id)})
            if user:
                return {
                    "status": 200,
                    "message": "User retrieved successfully.",
                    "data": user
                }
            else:
                return {
                    "status": 404,
                    "message": f"User with ID {user_id} not found."
                }
        except:
            return {"status": 500, "message": "Internal server error"}

    def updateProfile(self) -> Dict[str, Union[str, Any]]:
        try:
            if self.user_id is None:
                return {
                    "status": 400,
                    "message": "User ID is required to update a user."
                }

            update_data = {}

            if self.name:
                update_data["name"] = self.name

            if self.username:
                update_data["username"] = self.username

            update_data["updated_at"] = datetime.now()

            if not update_data:
                return {
                    "status": 400,
                    "message": "No fields provided to update."
                }

            result = self.collection.update_one(
                {"_id": ObjectId(self.user_id)},
                {"$set": update_data}
            )

            if result.modified_count > 0:
                return {
                    "status": 200,
                    "message": f"User  '{self.username}' updated successfully."
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to update user '{self.username}' or no changes were made."
                }
        except:
            return {"status": 500, "message": "Internal server error"}

    def login(self, email: str, password: str) -> Dict[str, Union[str, Any]]:
        try:
            user = self.collection.find_one({"email": email})

            if not user:
                return {    
                    "status": 404,
                    "message": "User not found."
                }
            
            if user.get("verified_at") is None:
                return {
                    "status": 403,
                    "message": "User does not have a verified account."
                }
            
            if user.get("is_active") is False:
                return {
                    "status": 403,
                    "message": "User account is disabled."
                }
            
            stored_password = user["password"]
            if verify_password(stored_password, password):
                self.user_id = str(user["_id"])  
                self.username = user["username"]
                self.password = stored_password  
                session_data = {
                    'user_id': self.user_id,
                    'exp': datetime.utcnow() + timedelta(days=3)  
                }

                token = jwt.encode(session_data, os.getenv('JWT_SECRET'), algorithm="HS256")

                return {
                    "status": 200,
                    "message": "Login successful.",
                    "token": token
                }
            else:
                return {
                    "status": 403,
                    "message": "Invalid username or password."
                }                
        except:
            return {"status": 500, "message": "Internal server error"}
        
    def change_password(self, old_password: str, new_password: str) -> Dict[str, Union[str, Any]]:
        try:
            user = self.collection.find_one({"_id": ObjectId(self.user_id)})

            if not user:
                return {"status": 404, "message": "User not found."}

            if not verify_password(user["password"], old_password):
                return {"status": 403, "message": "Invalid old password."}

            self.collection.update_one({ "_id": ObjectId(self.user_id) }, { "$set": {"password": hash_password(new_password)} })

            return {"status": 200, "message": "Password changed successfully."}
        except:
            return {"status": 500, "message": "Internal server error"}



    def get_current_session(self, token: str) -> Dict[str, Union[str, Any]]:
        try:
            session_data = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
            return {
                "status": 200,
                "message": "Session retrieved successfully.",
                "data": session_data
            }
        except jwt.ExpiredSignatureError:
            return {
                "status": 401,
                "message": "Session expired. Please log in again."
            }
        except jwt.InvalidTokenError:
            return {
                "status": 403,
                "message": "Invalid session token."
            }
        except:
            return {"status": 500, "message": "Internal server error"}
    
    def handle_request_verify_email(self) -> Dict[str, Union[str, Any]]:
        try:
            collectionUser = db.get_collection("users")
            collectionToken = db.get_collection("token")

            user =  collectionUser.find_one({"email": self.email})

            if user is None:
                return {
                    "status": 400,
                    "detail": "Email not found"
                }
        
            if "verified_at" in user and user["verified_at"] is not None:
                return {
                    "status": 400,
                    "detail": "Email already active"
                }

            last_request = collectionToken.find_one({
                "user_id": user["_id"],
                "created_at": {"$gte": datetime.now() - timedelta(minutes=2)}
            })

            if last_request:
                return {
                    "status": 400,
                    "detail": "Verification request already submitted within 2 minutes"
                }
        
            tokendoc = collectionToken.insert_one({
                "user_id": user["_id"],
                "type" : "verification",
                "created_at": datetime.now(),
            })

            token_id = str(tokendoc.inserted_id)
            base_url = os.getenv("BASE_URL", "http://127.0.0.1:8000/api/v1")
            activation_link = f"{base_url}/auth/verify/{token_id}"
            
            notifier = ActivationNotification()
            notifier.send_notification(recipient_email=user["email"], recipient_name=user["name"], activation_link=activation_link)
            return {"status": 200, "message": "Activation email sent successfully."}
        except:
            return {"status": 500, "detail": "Internal server error"}
    
    def handle_verify_email(self, token: str) -> Dict[str, Union[str, Any]]:
        try:
            collectionUser = db.get_collection("users")
            collectionToken = db.get_collection("token")

            token = collectionToken.find_one_and_delete({
                "_id": ObjectId(token),
                "type": "verification",
                "created_at": {
                    "$gte": datetime.now() - timedelta(minutes=2)
                }
            })

            if token is None:
                return {"status": 404, "detail": "Token not found"}
            
            user = collectionUser.find_one({"_id": token["user_id"]})
            
            if user is None:
                return {"status": 404, "detail": "User not found"}
            
            if "verified_at" in user and user["verified_at"] is not None:
                return {
                    "status": 400,
                    "detail": "Account already active"
                }
            
            collectionUser.update_one({"_id": token["user_id"]}, {"$set": {"verified_at": datetime.now()}})
            
            return {"status": 200, "message": "Account activated successfully."}
        except:
            return {"status": 500, "message": "Internal server error"}
    
    def handle_request_reset_password_email(self) -> Dict[str, Union[str, Any]]:
        try:
            collectionUser = db.get_collection("users")
            collectionToken = db.get_collection("token")

            user =  collectionUser.find_one({"email": self.email})

            if user is None:
                return {
                    "status": 400,
                    "detail": "Email not found"
                }
        
            if "verified_at" not in user or user["verified_at"] is None:
                return {
                    "status": 400,
                    "detail": "Account not active"
                }

            last_request = collectionToken.find_one({
                "user_id": user["_id"],
                "type": "reset-password",
                "created_at": {"$gte": datetime.now() - timedelta(minutes=15)}
            })

            if last_request:
                return {
                    "status": 400,
                    "detail": "Reset password request already submitted within 2 minutes"
                }
        
            tokendoc = collectionToken.insert_one({
                "user_id": user["_id"],
                "type" : "reset-password",
                "created_at": datetime.now(),
            })

            token_id = str(tokendoc.inserted_id)
            base_url = os.getenv("BASE_URL", "http://127.0.0.1:8000/api/v1")
            reset_password_link = f"{base_url}/auth/reset-password/{token_id}"
            
            notifier = ResetPasswordNotification()
            notifier.send_notification(user["email"], user["name"], reset_password_link)
            return {"status": 200, "message": "Reset password email sent successfully."}
        except:
            return {"status": 500, "detail": "Internal server error"}

    def handle_reset_password(self, token: str) -> Dict[str, Union[str, Any]]:
        try:
            collectionUser = db.get_collection("users")
            collectionToken = db.get_collection("token")

            token = collectionToken.find_one_and_delete({
                "_id": ObjectId(token),
                "type": "reset-password",
                "created_at": {"$gte": datetime.now() - timedelta(minutes=15)}
            })

            if token is None:
                return {"status": 404, "detail": "Token not found"}
            
            user = collectionUser.find_one({"_id": token["user_id"]})
            
            if user is None:
                return {"status": 404, "detail": "User not found"}
            
            collectionUser.update_one({"_id": token["user_id"]}, {"$set": {"password": hash_password(self.password), "updated_at": datetime.now()}})

            return {"status": 200, "message": "Password changed successfully."}
        except:
            return {"status": 500, "message": "Internal server error"}
    
    async def upload_profile_picture(self, image: str) -> Dict[str, Union[str, Any]]:
        try:
            collectionUser = db.get_collection("users")
        
            decoded_bytes = base64.b64decode(image, validate=True)

            if base64.b64encode(decoded_bytes).decode("utf-8") != image:
                return {"status": 400, "message": "Invalid image file."}

            if len(decoded_bytes) > 512 * 1024:
                return {"status": 400, "message": "File size exceeds the 512KB limit."}

            async with aiohttp.ClientSession() as session:
                async with session.post("https://api.imgbb.com/1/upload", data={
                    "key": os.getenv("IMGBB_API_KEY"),
                    "image": image
                }) as response:
                    if response.status != 200:
                        return {"status": 400, "message": "Failed to update image"}
                    
                    json_response = await response.json()

                    collectionUser.update_one({
                        "_id": ObjectId(self.user_id)
                    }, {
                        "$set": {
                            "profile_image": json_response["data"]["url"],
                            "updated_at": datetime.now()
                        }
                    })

                    return {"status": 200, "message": "Image changed successfully.", "data": json_response["data"]["url"]}
        except:
            return {"status": 500, "message": "Internal server error"}