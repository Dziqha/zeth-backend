from datetime import datetime, timedelta
from typing import Any, Dict, Union
from bson import ObjectId
from .userEntityModel import UserEntityModel
from ...configs.database import db_instance as db

class Agenda(UserEntityModel):
    def __init__(self, agenda_id: str = None, user_id: str = None, name: str = None, description: str = None, category: str = None, date: datetime = None, start_time: datetime = None, end_time: datetime = None, location: str = None):
        super().__init__(user_id=user_id, category=category)
        self.agenda_id = agenda_id
        self.name = name
        self.description = description
        self.category = category
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location  
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.collection = db.get_collection("agendas")
        self.category_collection = db.get_collection("categories")
    
    
    def create(self) -> Dict[str, Union[str, Any]]:
        try:
            categoryid = self.category_collection.find_one({"_id": ObjectId(self.category), "user_id": ObjectId(self.user_id)})
            if not categoryid:
                return {
                    "status": 404,
                    "message": f"Category '{self.category}' not found."
                }
            self.category = categoryid['_id']

            agendaData = {
                "user_id": ObjectId(self.user_id),
                "name": self.name,
                "description": self.description,
                "category": self.category,
                "date": self.date,
                "start_time": self.start_time,
                "end_time": self.end_time,
                "location": self.location,
                "created_at": self.created_at
            }

            result = self.collection.insert_one(agendaData)
            if result.inserted_id:
                return {
                    "status": 200,
                    "message": f"Agenda '{self.name}' created successfully.",
                    "data": {
                        "_id": str(result.inserted_id),
                        "user_id": str(self.user_id),
                        "name": self.name,
                        "description": self.description,
                        "category": str(self.category),
                        "date": str(self.date),
                        "start_time": self.start_time,
                        "end_time": self.end_time,
                        "location": self.location,
                        "created_at": str(self.created_at)
                    }
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to create agenda '{self.name}'."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}

    def update(self, agenda_id: str) -> Dict[str, Union[str, Any]]:
        try:
            agenda = self.collection.find_one({"_id": ObjectId(agenda_id), "user_id": ObjectId(self.user_id)})
            if not agenda:
                return {
                    "status": 404,
                    "message": f"Agenda with ID '{agenda_id}' not found."
                }

            update_data = {}

            if self.name:
                update_data["name"] = self.name

            if self.description:
                update_data["description"] = self.description

            if self.category:
                categoryid = self.category_collection.find_one({"_id": ObjectId(self.category), "user_id": ObjectId(self.user_id)})
                if not categoryid:
                    return {
                        "status": 404,
                        "message": f"Category '{self.category}' not found."
                    }
                update_data["category"] = categoryid["_id"]

            if self.date:
                update_data["date"] = self.date

            if self.start_time:
                update_data["start_time"] = self.start_time

            if self.end_time:
                update_data["end_time"] = self.end_time

            if self.location:
                update_data["location"] = self.location

            if self.updated_at is not None:
                    update_data["updated_at"] = self.updated_at

            if not update_data:
                return {
                    "status": 400,
                    "message": "No fields provided to update."
                }

            result = self.collection.update_one({"_id": ObjectId(agenda_id)}, {"$set": update_data})
            if result.modified_count > 0:
                return {
                    "status": 200,
                    "message": f"Agenda with name '{self.name}' updated successfully."
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to update agenda with name '{self.name}'."
                }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}
        
    def get_all(self) -> list[dict[str, Any]]:
        try:
            agendas = self.collection.find({ "user_id": ObjectId(self.user_id) })
            if not agendas:
                return {
                    "status": 404,
                    "message": "No agendas found."
                }
            result = list(agendas)
            return {
                "status": 200,
                "message": "Agendas retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}

    def get_by_id(self, agenda_id: str) -> Dict[str, Union[str, Any]]:
        try:
            agenda = self.collection.find_one({"_id": ObjectId(agenda_id), "user_id": ObjectId(self.user_id) })
            if agenda:
                return {
                    "status": 200,
                    "message": "Agenda retrieved successfully.",
                    "data": agenda
                }
            else:
                return {
                    "status": 404,
                    "message": f"Agenda with ID '{agenda_id}' not found."
                }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}
    
    def get_by_category(self, category_id: str) -> list[dict[str, Any]]:
        try:
            agenda = self.collection.find({"category": ObjectId(category_id), "user_id": ObjectId(self.user_id)})
            if not agenda:
                return {
                    "status": 404,
                    "message": "No agendas found."
                }
            result = list(agenda)
            return {
                "status": 200,
                "message": "Agendas retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}
        
    def delete(self, agenda_id: str) -> Dict[str, Union[str, Any]]:
        try:
            agenda = self.collection.find_one({"_id": ObjectId(agenda_id), "user_id": ObjectId(self.user_id)})
            if agenda:
                result = self.collection.delete_one({"_id": ObjectId(agenda_id)})
                if result.deleted_count > 0:
                    return {
                        "status": 200,
                        "message": "Agenda deleted successfully."
                    }
                else:
                    return {
                        "status": 400,
                        "message": "Failed to delete agenda."
                    }
            else:
                return {
                    "status": 404,
                    "message": f"Agenda not found."
                }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}