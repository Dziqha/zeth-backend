from typing import Any, Dict
from fastapi import APIRouter,  Depends, HTTPException, Header, Path
from fastapi.responses import JSONResponse
from ..services.interface.schedule_interface_service import Schedule
from pydantic import BaseModel
from fastapi import Request
from ..middlewares.auth import require_auth

router = APIRouter()

class ScheduleRequest(BaseModel):
    name: str
    description: str
    category: str
    day: str
    start_time: str
    end_time: str
    location: str

@router.get("/schedule")
@require_auth
async def get_all_schedule(request: Request):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        schedules = Schedule()
        response = schedules.get_all(user_id=user_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        filter_response = {
            "status": response["status"],
            "data": [
                {
                    **{
                        "_id": str(row["_id"]),
                        "user_id": str(row["user_id"]),
                        "name": row.get("name"),
                        "description": row.get("description"),
                        "category": str(row["category"]),
                        "day": str(row["day"]),
                        "start_time": row.get("start_time"),
                        "end_time": row.get("end_time"),
                        "location": row.get("location"),
                        "created_at": row.get("created_at").isoformat()
                    },
                    **({"updated_at": row["updated_at"].isoformat()} if "updated_at" in row else {})
                }
                for row in response["data"]
            ]
        }
        return JSONResponse(filter_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/schedule")
@require_auth
async def create_schedule(request: Request, schedule: ScheduleRequest):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        schedule = Schedule(user_id=user_id, name= schedule.name, description= schedule.description, category= schedule.category, day= schedule.day,  start_time= schedule.start_time, end_time= schedule.end_time, location= schedule.location)
        response = schedule.create()
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/schedule/{schedule_id}')
@require_auth
async def get_schedule_by_id(request: Request, schedule_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        
        schedule = Schedule()
        response = schedule.get_by_id(schedule_id=schedule_id, user_id=user_id)
        if not response and "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        result = response["data"]
        filtered_response = {
            "status": response["status"],
            "data": {
                **{
                    "_id": str(result["_id"]),
                    "user_id": str(result["user_id"]),
                    "name": result.get("name"),
                    "description": result.get("description"),
                    "category": str(result["category"]),
                    "day": str(result["day"]),
                    "start_time": result.get("start_time"),
                    "end_time": result.get("end_time"),
                    "location": result.get("location"),
                     "created_at": result.get("created_at").isoformat()
                    },
                    **({"updated_at": result["updated_at"].isoformat()} if "updated_at" in result else {})
            }
        }

        return JSONResponse(filtered_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/schedule/category/{category_id}')
@require_auth
async def get_schedule_by_category(request: Request, category_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        schedule = Schedule()
        response = schedule.get_by_category(category_id=category_id, user_id=user_id)
        filtered_response = {
            "status": response["status"],
            "data": [
                {
                    **{
                        "_id": str(row["_id"]),
                        "user_id": str(row["user_id"]),
                        "name": row.get("name"),
                        "description": row.get("description"),
                        "category": str(row["category"]),
                        "day": str(row["day"]),
                        "start_time": row.get("start_time"),
                        "end_time": row.get("end_time"),
                        "location": row.get("location"),
                        "created_at": row.get("created_at").isoformat()
                    },
                    **({"updated_at": row["updated_at"].isoformat()} if "updated_at" in row else {})
                }
                for row in response["data"]
            ]
        }

        return JSONResponse(filtered_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/schedule/{schedule_id}')
@require_auth
async def update_schedule(
    request: Request,
    schedule_id: str = Path(...),
    schedule_data: Dict[str, Any] = None
):
    
    try:
        session = request.state.session
        user_id = session.get("user_id")

        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        allowed_keys = {"name", "description", "category", "day", "start_time", "end_time", "location"}
        if not set(schedule_data.keys()).issubset(allowed_keys):
            raise HTTPException(
                status_code=400,
                detail=f"Only {', '.join(allowed_keys)} can be updated."
            )
        name = schedule_data.get("name")
        description = schedule_data.get("description")
        category = schedule_data.get("category")
        day = schedule_data.get("day")
        start_time = schedule_data.get("start_time")
        end_time = schedule_data.get("end_time")
        location = schedule_data.get("location")

        schedule = Schedule(user_id=user_id, name= name, description= description, category= category, day= day,  start_time= start_time, end_time= end_time, location= location)
        response = schedule.update(schedule_id)
        return JSONResponse(response, status_code=response["status"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.delete('/schedule/{schedule_id}')
@require_auth
async def delete_schedule(request: Request, schedule_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        scedule = Schedule()
        response = scedule.delete(schedule_id=schedule_id, user_id=user_id)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))