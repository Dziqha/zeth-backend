from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, Header, Path
from fastapi.responses import JSONResponse
from ..services.interface.notes_interface_service import Notes
from pydantic import BaseModel
from fastapi import Request
from ..middlewares.auth import require_auth

router = APIRouter()

class CreateNoteRequest(BaseModel):
    title: str
    category: str
    content: str

@router.post("/notes")
@require_auth
async def create_note(request: Request, note_data: CreateNoteRequest):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        note = Notes(user_id=user_id, title=note_data.title, category=note_data.category, content=note_data.content)
        response = note.create()
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    

@router.get("/notes")
@require_auth
async def get_all_notes(request: Request):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        notes = Notes()
        response = notes.get_all(user_id=user_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        
        fitered_response = {
            "status": response["status"],
            "data": [
                {
                    **{
                        "_id": str(row["_id"]),
                        "user_id": str(row["user_id"]),
                        "title": row.get("title"),
                        "category": str(row["category"]),
                        "content": row.get("content"),
                        "created_at": row.get("created_at").isoformat()
                    },
                    **({"updated_at": row["updated_at"].isoformat()} if "updated_at" in row else {})
                }
                for row in response["data"]
            ]
        }

        return JSONResponse(fitered_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@router.get('/notes/{note_id}')
@require_auth
async def get_note_by_id(request: Request, note_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        note = Notes()
        response = note.get_by_id(note_id=note_id, user_id=user_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        
        result = response["data"]
        fitered_response = {
            "status": response["status"],
            "data": {
                **{
                    "_id": str(result["_id"]),
                    "user_id": str(result["user_id"]),
                    "title": result.get("title"),
                    "category": str(result["category"]),
                    "content": result.get("content"),
                    "created_at": result.get("created_at").isoformat()
                    },
                    **({"updated_at": result["updated_at"].isoformat()} if "updated_at" in result else {})
            }
        }

        return JSONResponse(fitered_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/notes/category/{category_id}')
@require_auth
async def get_note_by_category(request: Request, category_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        notes = Notes()
        response = notes.get_by_category(category_id=category_id, user_id=user_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        
        fitered_response = {
            "status": response["status"],
            "data": [
                {
                    **{
                        "_id": str(row["_id"]),
                        "user_id": str(row["user_id"]),
                        "title": row.get("title"),
                        "category": str(row["category"]),
                        "content": row.get("content"),
                        "created_at": row.get("created_at").isoformat()
                    },
                    **({"updated_at": row["updated_at"].isoformat()} if "updated_at" in row else {})
                }
                for row in response["data"]
            ]
        }

        return JSONResponse(fitered_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/notes/{note_id}')
@require_auth
async def update_note(
    request: Request,
    note_id: str = Path(...),
    note_data: Dict[str, Any] = None
):
    
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")
        
        allowed_keys = {"title", "category", "content"}
        if not set(note_data.keys()).issubset(allowed_keys):
            raise HTTPException(
                status_code=400,
                detail=f"Only {', '.join(allowed_keys)} can be updated."
            )
        title = note_data.get("title")
        category = note_data.get("category")
        content = note_data.get("content")

        note = Notes(note_id=note_id, user_id=user_id, title=title, category=category, content=content)
        response = note.update(note_id)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.delete('/notes/{note_id}')
@require_auth
async def delete_note(request: Request, note_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        note = Notes()
        response = note.delete(note_id=note_id, user_id=user_id)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))