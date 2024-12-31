from datetime import datetime
from typing import Any, Dict, Union
from bson import ObjectId
from .userEntityModel import UserEntityModel
from ...configs.database import db_instance as db

class Notes(UserEntityModel):
    def __init__(self, note_id : str = None, user_id : str = None, title : str = None, category : str = None, content : str = None):
        super().__init__(user_id=user_id,category=category)
        self.note_id = note_id
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.collection = db.get_collection('notes')
        self.category_collection = db.get_collection('categories')
    
    def create(self)-> Dict[str, Union[str, Any]]:
        try:
            categoryid = self.category_collection.find_one({"_id": ObjectId(self.category)})
            if not categoryid:
                return {
                    "status": 404,
                    "message": f"Category '{self.category}' not found."
                }
            self.category = categoryid['_id']
            noteData = {
                "user_id": ObjectId(self.user_id),
                "title": self.title,
                "category": self.category,
                "content": self.content,
                "created_at": self.created_at
            }
            result = self.collection.insert_one(noteData)
            if result.inserted_id:
                return {
                    "status": 200,
                    "message": f"Note '{self.title}' created successfully.",
                    "data": {
                        "_id": str(result.inserted_id),
                        "user_id": str(self.user_id),
                        "title": self.title,
                        "category": str(self.category),
                        "content": self.content,
                        "created_at": str(self.created_at)
                    }
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to create note '{self.title}'."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}


    def update(self, note_id: str)-> Dict[str, Union[str, Any]]:
        try:
            note = self.collection.find_one({"_id": ObjectId(note_id), "user_id": ObjectId(self.user_id)})
            if note:
                update_data = {}
                if self.title:
                    update_data["title"] = self.title
                if self.category:
                    category_data = self.category_collection.find_one({"_id": ObjectId(self.category)})
                    if not category_data:
                        return {
                            "status": 404,
                            "message": f"Category '{self.category}' not found."
                        }
                    update_data["category"] = category_data["_id"]
                if self.content:
                    update_data["content"] = self.content
                if self.updated_at is not None:
                    update_data["updated_at"] = self.updated_at
                if not update_data:
                    return {
                        "status": 400,
                        "message": "No fields provided to update."
                    }
                result = self.collection.update_one({"_id": ObjectId(note_id)}, {"$set": update_data})
                if result.modified_count > 0:
                    return {
                        "status": 200,
                        "message": f"Note updated with title '{self.title}' successfully."
                    }
                else:
                    return {
                        "status": 400,
                        "message": f"Failed to update note with title '{self.title}'."
                }
            else:
                return {
                    "status": 404,
                    "message": f"Note with ID '{note_id}' not found."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}

    
    def get_all(self, user_id: str) -> list[dict[str, Any]]:
        try:
            notes = self.collection.find({ "user_id": ObjectId(user_id) })
            if not notes:
                return {
                    "status": 404,
                    "message": "No notes found."
                }
            result = list(notes)
            return {
                "status": 200,
                "message": "Notes retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}


    def get_by_id(self, note_id: str, user_id: str)-> Dict[str, Union[str, Any]]:
        try:
            note = self.collection.find_one({"_id": ObjectId(note_id), "user_id": ObjectId(user_id)})
            if note:
                return {
                    "status": 200,
                    "message": "Note retrieved successfully.",
                    "data": note
                }
            else:
                return {
                    "status": 404,
                    "message": f"Note with ID '{note_id}' not found."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}
    
    def get_by_category(self, category_id: str, user_id: str)-> list[dict[str, Any]]:
        try:
            note = self.collection.find({"category": ObjectId(category_id), "user_id": ObjectId(user_id)})
            if not note:
                return {
                    "status": 404,
                    "message": "No notes found."
                }
            result = list(note)
            return {
                "status": 200,
                "message": "Notes retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}
        
    def delete(self, note_id: str, user_id: str)-> Dict[str, Union[str, Any]]:
        try:
            note = self.collection.find_one({"_id": ObjectId(note_id), "user_id": ObjectId(user_id)})
            if note:
                result = self.collection.delete_one({"_id": ObjectId(note_id), "user_id": ObjectId(user_id)})
                if result.deleted_count > 0:
                    return {
                        "status": 200,
                        "message": "Note deleted successfully."
                    }
                else:
                    return {
                        "status": 400,
                        "message": "Failed to delete note."
                    }
            else:
                return {
                    "status": 404,
                    "message": f"Note with ID '{note_id}' not found."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}