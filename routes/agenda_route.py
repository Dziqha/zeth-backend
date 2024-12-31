from typing import Any, Dict
from fastapi import APIRouter, HTTPException,  Path
from fastapi.responses import JSONResponse
from ..services.interface.agenda_interface_service import Agenda
from pydantic import BaseModel
from fastapi import Request
from ..middlewares.auth import require_auth

router = APIRouter()

class AgendaRequest(BaseModel):
    name: str
    description: str
    category: str
    date: str
    start_time: str
    end_time: str
    location: str

@router.get("/agenda")
@require_auth
async def get_all_agenda(request: Request):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")
        
        agenda = Agenda(user_id=user_id)
        response = agenda.get_all()
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
                        "date": row.get("date"),
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


@router.post("/agenda")
@require_auth
async def create_agenda(request: Request, agenda: AgendaRequest):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        agenda = Agenda(user_id=user_id, name=agenda.name, description=agenda.description, category=agenda.category, date=agenda.date, start_time=agenda.start_time, end_time=agenda.end_time, location=agenda.location)
        response = agenda.create()
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/agenda/{agenda_id}')
@require_auth
async def get_agenda_by_id(request: Request, agenda_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        agenda = Agenda(user_id=user_id)
        response = agenda.get_by_id(agenda_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        
        result = response["data"]
        filtered_response = {
            "status": response["status"],
            "data": 
                {
                    **{
                        "_id": str(result["_id"]),
                        "user_id": str(result["user_id"]),
                        "name": result.get("name"),
                        "description": result.get("description"),
                        "category": str(result["category"]),
                        "date": result.get("date"),
                        "start_time": result.get("start_time"),
                        "end_time": result.get("end_time"),
                        "location": result.get("location"),
                        "created_at": result.get("created_at").isoformat()
                    },
                    **({"updated_at": result["updated_at"].isoformat()} if "updated_at" in result else {})
                }}

        return JSONResponse(filtered_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/agenda/category/{category_id}')
@require_auth
async def get_agenda_by_category(request: Request, category_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        agenda = Agenda(user_id=user_id)
        response = agenda.get_by_category(category_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
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
                        "date": row.get("date"),
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

@router.put('/agenda/{agenda_id}')
@require_auth
async def update_agenda(
    request: Request,
    agenda_id: str = Path(...),
    agenda_data: Dict[str, Any] = None
):
    
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        allowed_keys = {"name", "description", "category", "date", "start_time", "end_time", "location"}
        if not set(agenda_data.keys()).issubset(allowed_keys):
            raise HTTPException(
                status_code=400,
                detail=f"Only {', '.join(allowed_keys)} can be updated."
            )
        name = agenda_data.get("name")
        description = agenda_data.get("description")
        category = agenda_data.get("category")
        date = agenda_data.get("date")
        start_time = agenda_data.get("start_time")
        end_time = agenda_data.get("end_time")
        location = agenda_data.get("location")

        agenda = Agenda( agenda_id=agenda_id,user_id=user_id, name=name, description=description, category=category, date=date, start_time=start_time, end_time=end_time, location=location)
        response = agenda.update(agenda_id=agenda_id)
        return JSONResponse(response, status_code=response["status"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.delete('/agenda/{agenda_id}')
@require_auth
async def delete_agenda(request: Request, agenda_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        agenda = Agenda(user_id=user_id)
        response = agenda.delete(agenda_id)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))