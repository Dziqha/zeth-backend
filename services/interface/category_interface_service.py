from datetime import datetime
from typing import Any, Dict, Union
from bson import ObjectId
from .userEntityModel import UserEntityModel
from ...configs.database import db_instance as db

class Category(UserEntityModel):
    def __init__(self , user_id : str = None, category_id : str = None, name : str = None, description : str = None, icon : str = None, color : str = None):
        self.category_id = category_id
        super().__init__(user_id=user_id, name=name)
        self.description = description
        self.icon = icon
        self.color = color
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.collection = db.get_collection('categories')

    def create(self)-> Dict[str, Union[str, Any]]:
        try:
            categoryData = {
                "name": self.name,
                "user_id": ObjectId(self.user_id),
                "description": self.description,
                "icon": self.icon,
                "color": self.color,
                "created_at": self.created_at
            }
            result = self.collection.insert_one(categoryData)
            if result.inserted_id:
                return {
                    "status": 200,
                    "message": f"Category '{self.name}' created successfully.",
                    "data": {
                        "_id": str(result.inserted_id),
                        "name": self.name,
                        "user_id": self.user_id,
                        "description": self.description,
                        "icon": self.icon,
                        "color": self.color,
                        "created_at": str(self.created_at)
                    }
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to create category '{self.name}'."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}
        
    def get_all(self, user_id: str)-> Dict[str, Union[str, Any]]:
        try:
            categories = self.collection.find({ "user_id": ObjectId(user_id) })
            result = list(categories)
            if not categories:
                return {
                    "status": 404,
                    "message": "No categories found."
                }
            return {
                "status": 200,
                "message": "Categories retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}

    def get_by_id(self, category_id: str, user_id: str)-> Dict[str, Union[str, Any]]:
        try:
            category = self.collection.find_one({"_id": ObjectId(category_id), "user_id": ObjectId(user_id) })
            if category:
                return {
                    "status": 200,
                    "message": "Category retrieved successfully.",
                    "data": category
                }
            else:
                return {
                    "status": 404,
                    "message": f"Category with ID '{category_id}' not found."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}

    def update(self, category_id: str)-> Dict[str, Union[str, Any]]:
        try:
            category = self.collection.find_one({"_id": ObjectId(category_id), "user_id": ObjectId(self.user_id)})
            if category:
                update_data = {}
                if self.name:
                    update_data["name"] = self.name
                if self.category:
                    update_data["category"] = self.category
                if self.description:
                    update_data["description"] = self.description
                if self.icon:
                    update_data["icon"] = self.icon
                if self.color:
                    update_data["color"] = self.color
                if self.updated_at is not None:
                    update_data["updated_at"] = self.updated_at
                if not update_data:
                    return {
                        "status": 400,
                        "message": "No fields provided to update."
                    }
                result = self.collection.update_one({"_id": ObjectId(category_id)}, {"$set": update_data})
                if result.modified_count > 0:
                    return {
                        "status": 200,
                        "message": f"Category with name '{self.name}' updated successfully."
                    }
                else:
                    return {
                        "status": 400,
                        "message": f"Failed to update with name '{self.name}' category."
                }
            else:
                return {
                    "status": 404,
                    "message": f"Category with ID '{category_id}' not found."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}
        
    def delete(self, category_id: str, user_id: str)-> Dict[str, Union[str, Any]]:
        try:
            category = self.collection.find_one({"_id": ObjectId(category_id), "user_id": ObjectId(user_id)})
            if category:
                result = self.collection.delete_one({"_id": ObjectId(category_id)})
                if result.deleted_count == 0:
                    return {
                        "status": 400,
                        "message": "Failed to delete category."
                    }
                
                db.get_collection("agendas").delete_many({
                    "category": ObjectId(category_id)
                })

                db.get_collection("notes").delete_many({
                    "category": ObjectId(category_id)
                })

                db.get_collection("schedules").delete_many({
                    "category": ObjectId(category_id)
                })

                db.get_collection("todos").delete_many({
                    "category": ObjectId(category_id)
                })

                return {
                    "status": 200,
                    "message": "Category deleted successfully."
                }  
                    
            else:
                return {
                    "status": 404,
                    "message": f"Category with ID '{category_id}' not found."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}
        
    def get_by_category(self, category_id: str) -> Dict[str, Union[str, Any]]:
        pass