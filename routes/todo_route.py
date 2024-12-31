from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, Header, Path
from fastapi.responses import JSONResponse
from ..services.interface.todo_interface_service import Todo
from pydantic import BaseModel
from fastapi import Request
from ..middlewares.auth import require_auth

router = APIRouter()

class TodoRequest(BaseModel):
    name: str
    description: str
    category: str
    status: str
    due_date: str

@router.get("/todo")
@require_auth
async def get_all_todos(request: Request):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        todos = Todo()
        response = todos.get_all(user_id=user_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        fiter_response = {
            "status": response["status"],
            "data": [
                {
                    **{
                        "_id": str(row["_id"]),
                        "user_id": str(row["user_id"]),
                        "name": row.get("name"),
                        "description": row.get("description"),
                        "category": str(row["category"]),
                        "status": str(row["status"]),
                        "due_date": row.get("due_date"),
                        "created_at": row.get("created_at").isoformat()
                    },
                    **({"updated_at": row["updated_at"].isoformat()} if "updated_at" in row else {})
                }
                for row in response["data"]
            ]
         }
        return JSONResponse(fiter_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/todo")
@require_auth
async def create_todo(request: Request, todo: TodoRequest):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        todo = Todo(user_id=user_id, name=todo.name, description=todo.description, category=todo.category, status=todo.status, due_date=todo.due_date)
        response = todo.create()
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/todo/{todo_id}')
@require_auth
async def get_todo_by_id(request: Request, todo_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        todo = Todo()
        response = todo.get_by_id(todo_id=todo_id, user_id=user_id)
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
                        "status": str(result["status"]),
                        "due_date": result.get("due_date"),
                        "created_at": result.get("created_at").isoformat()
                    },
                    **({"updated_at": result["updated_at"].isoformat()} if "updated_at" in result else {})
                }
            }

        return JSONResponse(filtered_response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/todo/category/{category_id}')
@require_auth
async def get_todo_by_category(request: Request, category_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        todo = Todo()
        response = todo.get_by_category(category_id=category_id, user_id=user_id)
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
                        "status": str(row["status"]),
                        "due_date": row.get("due_date"),
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

@router.put('/todo/{todo_id}')
@require_auth
async def update_todo(
    request: Request,
    todo_id: str = Path(...),
    todo_data: Dict[str, Any] = None
):
    
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        allowed_keys = {"name", "description", "category", "status", "due_date"}
        if not set(todo_data.keys()).issubset(allowed_keys):
            raise HTTPException(
                status_code=400,
                detail=f"Only {', '.join(allowed_keys)} can be updated."
            )
        name = todo_data.get("name")
        description = todo_data.get("description")
        category = todo_data.get("category")
        status = todo_data.get("status")
        due_date = todo_data.get("due_date")

        todo = Todo(todo_id=todo_id, user_id=user_id, name=name, description=description, category=category, status=status, due_date=due_date)
        response = todo.update(todo_id)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.delete('/todo/{todo_id}')
@require_auth
async def delete_todo(request: Request, todo_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        todo = Todo()
        response = todo.delete(todo_id=todo_id, user_id=user_id)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))