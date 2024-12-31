from datetime import datetime, timedelta
from typing import Any, Dict, Union
from bson import ObjectId
from .userEntityModel import UserEntityModel
from ...configs.database import db_instance as db

class Schedule(UserEntityModel):
    def __init__(self, schedule_id: str = None, user_id: str = None, name: str = None, description: str = None, category: str = None, day : str = None, start_time: datetime = None, end_time: datetime = None, location: str = None):
        super().__init__(user_id=user_id, category=category)
        self.schedule_id = schedule_id
        self.name = name
        self.description = description
        self.category = category
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.location = location  
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.collection = db.get_collection("schedules")
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

            scheduleData = {
                "user_id": ObjectId(self.user_id),
                "name": self.name,
                "description": self.description,
                "category": self.category,
                "day": self.day,
                "start_time": self.start_time,
                "end_time": self.end_time,
                "location": self.location,
                "created_at": self.created_at
            }

            result = self.collection.insert_one(scheduleData)
            if result.inserted_id:
                return {
                    "status": 200,
                    "message": f"Schedule '{self.name}' created successfully.",
                    "data": {
                        "_id": str(result.inserted_id),
                        "user_id": str(self.user_id),
                         "name": self.name,
                        "description": self.description,
                        "category": str(self.category),
                        "day": self.day,
                        "start_time": self.start_time,
                        "end_time": self.end_time,
                        "location": self.location,
                        "created_at": str(self.created_at)
                    }
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to create schedule '{self.name}'."
                }
        except Exception as e:
            return  {"status": 500, "message": "Internal server error"}

    def update(self, schedule_id: str) -> Dict[str, Union[str, Any]]:
        try:
            schedule = self.collection.find_one({"_id": ObjectId(schedule_id), "user_id": ObjectId(self.user_id)})
            if not schedule:
                return {
                    "status": 404,
                    "message": f"Schedule with ID '{schedule_id}' not found."
                }

            update_data = {}

            if self.name:
                update_data["name"] = self.name

            if self.description:
                update_data["description"] = self.description

            if self.category:
                categoryid = self.category_collection.find_one({"_id": ObjectId(self.category)})
                if not categoryid:
                    return {
                        "status": 404,
                        "message": f"Category '{self.category}' not found."
                    }
                update_data["category"] = categoryid["_id"]

            if self.day:
                update_data["day"] = self.day

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

            result = self.collection.update_one({"_id": ObjectId(schedule_id)}, {"$set": update_data})
            if result.modified_count > 0:
                return {
                    "status": 200,
                    "message": f"Schedule with name '{self.name}' updated successfully."
                }
            else:
                return {
                    "status": 400,
                    "message": f"Failed to update schedule with name '{self.name}'."
                }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}
        
    def get_all(self, user_id: str) -> list[dict[str, Any]]:
        try:
            schedules = self.collection.find({ "user_id": ObjectId(user_id) })
            if not schedules:
                return {
                    "status": 404,
                    "message": "No schedules found."
                }
            result = list(schedules)
            return {
                "status": 200,
                "message": "Schedules retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}

    def get_by_id(self, schedule_id: str, user_id: str) -> Dict[str, Union[str, Any]]:
        try:
            schedule = self.collection.find_one({"_id": ObjectId(schedule_id), "user_id": ObjectId(user_id)})
            if schedule :
                return {
                    "status": 200,
                    "message": "Schedule retrieved successfully.",
                    "data": schedule
                }
            else:
                return {
                    "status": 404,
                    "message": f"Schedule with ID '{schedule_id}' not found."
                }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}
    
    def get_by_category(self, category_id: str, user_id: str) -> list[dict[str, Any]]:
        try:
            schedule = self.collection.find({"category": ObjectId(category_id), "user_id": ObjectId(user_id)})
            if not schedule:
                return {
                    "status": 404,
                    "message": "No schedules found."
                }
            result = list(schedule)
            return {
                "status": 200,
                "message": "Schedules retrieved successfully.",
                "data": result
            }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}
        
    def delete(self, schedule_id: str, user_id: str) -> Dict[str, Union[str, Any]]:
        try:
            schedule = self.collection.find_one({"_id": ObjectId(schedule_id), "user_id": ObjectId(user_id)})
            if schedule:
                result = self.collection.delete_one({"_id": ObjectId(schedule_id), "user_id": ObjectId(user_id)})
                if result.deleted_count > 0:
                    return {
                        "status": 200,
                        "message": "Schedule deleted successfully."
                    }
                else:
                    return {
                        "status": 400,
                        "message": "Failed to delete schedule."
                    }
            else:
                return {
                    "status": 404,
                    "message": f"Schedule with ID '{schedule_id}' not found."
                }
        except Exception as e:
            return {"status": 500, "message": "Internal server error"}