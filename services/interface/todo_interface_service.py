from datetime import datetime, timedelta
from typing import Any, Dict, Union
from bson import ObjectId
from .userEntityModel import UserEntityModel
from ...configs.database import db_instance as db

class Todo(UserEntityModel):
    def __init__(self, todo_id: str = None, user_id: str = None, name: str = None, description: str = None, category: str = None, status: str = None, due_date: datetime = None):
        super().__init__(user_id=user_id, category=category)
        self.todo_id = todo_id
        self.name = name
        self.description = description
        self.status = status
        self.category = category
        self.due_date = due_date  
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.collection = db.get_collection("todos")
        self.category_collection = db.get_collection("categories")
    
    
    def create(self) -> Dict[str, Union[str, Any]]:
        try: 
            categoryid = self.category_collection.find_one({"_id": ObjectId(self.category)})
            if not categoryid:
                return {
                    "status": 404,
                    "message": f"Category '{self.category}' not found."
                }
            self.category = categoryid['_id']

            todoData = {
                "user_id": ObjectId(self.user_id),
                "name": self.name,
                "description": self.description,
                "category": self.category,
                "status": self.status,
                "due_date": self.due_date,
                "created_at": self.created_at
            }

            result = self.collection.insert_one(todoData)
            if result.inserted_id:
                return {
                    "status": 200,
                    "message": f"Todo '{self.name}' created successfully.",
                    "data": {
                        "_id": str(result.inserted_id),
                        "user_id": str(self.user_id),
                        "name": self.name,
                        "description": self.description,
                        "category": str(self.category),
                        "status": self.status,
                        "due_date": str(self.due_date),
                        "created_at": str(self.created_at)
                    }
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to create todo '{self.name}'."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}

    def update(self, todo_id: str) -> Dict[str, Union[str, Any]]:
        try:
            todo = self.collection.find_one({"_id": ObjectId(todo_id), "user_id": ObjectId(self.user_id)})
            if not todo:
                return {
                    "status": 404,
                    "message": f"Todo with ID '{todo_id}' not found."
                }

            update_data = {}

            if self.name:
                update_data["name"] = self.name
            if self.description:
                update_data["description"] = self.description
            if self.status:
                update_data["status"] = self.status
            if self.category:
                categoryid = self.category_collection.find_one({"_id": ObjectId(self.category)})
                if not categoryid:
                    return {
                        "status": 404,
                        "message": f"Category '{self.category}' not found."
                    }
                update_data["category"] = categoryid["_id"]

            if self.due_date:
                update_data["due_date"] = self.due_date

            if self.updated_at is not None:
                    update_data["updated_at"] = self.updated_at

            if not update_data:
                return {
                    "status": 400,
                    "message": "No fields provided to update."
                }

            result = self.collection.update_one({"_id": ObjectId(todo_id)}, {"$set": update_data})
            if result.modified_count > 0:
                return {
                    "status": 200,
                    "message": f"Todo with name '{self.name}' updated successfully."
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to update Todo with name '{self.name}'."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}
        
    def get_all(self, user_id: str) -> list[dict[str, Any]]:
        try:
            todos = self.collection.find({ "user_id": ObjectId(user_id) })
            if not todos:
                return {
                    "status": 404,
                    "message": "No todos found."
                }
            result = list(todos)
            return {
                "status": 200,
                "message": "Todos retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}

    def get_by_id(self, todo_id: str, user_id: str) -> Dict[str, Union[str, Any]]:
        try:
            todo = self.collection.find_one({"_id": ObjectId(todo_id), "user_id": ObjectId(user_id) })
            if todo:
                return {
                    "status": 200,
                    "message": "Todo retrieved successfully.",
                    "data": todo
                }
            else:
                return {
                    "status": 404,
                    "message": f"Todo with ID '{todo_id}' not found."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}
    
    def get_by_category(self, category_id: str, user_id: str) -> list[dict[str, Any]]:
        try:
            todos = self.collection.find({"category": ObjectId(category_id), "user_id": ObjectId(user_id) })
            if not todos:
                return {
                    "status": 404,
                    "message": "No todos found."
                }
            result = list(todos)
            return {
                "status": 200,
                "message": "Todos retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}
            
    def delete(self, todo_id: str, user_id: str) -> Dict[str, Union[str, Any]]:
        try:
            todo = self.collection.find_one({"_id": ObjectId(todo_id), "user_id": ObjectId(user_id) })
            if todo:
                result = self.collection.delete_one({"_id": ObjectId(todo_id)})
                if result.deleted_count > 0:
                    return {
                        "status": 200,
                        "message": "Todo deleted successfully."
                    }
                else:
                    return {
                        "status": 400,
                        "message": "Failed to delete todo."
                    }
            else:
                return {
                    "status": 404,
                    "message": f"Todo with ID '{todo_id}' not found."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}