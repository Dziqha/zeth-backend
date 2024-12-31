from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, Header, Path
from fastapi.responses import JSONResponse
from ..services.interface.category_interface_service import Category
from pydantic import BaseModel
from fastapi import Request
from ..middlewares.auth import require_auth

router = APIRouter()


class CategoryRequest(BaseModel):
    name: str
    description: str
    icon: str
    color: str

@router.get("/category")
@require_auth
async def get_all_categories(request: Request):
    try:
        session = request.state.session
        user_id = session.get("user_id")

        category = Category()
        response = category.get_all(user_id=user_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        filter_data = {
            "status": response["status"],
            "message": response["message"],
            "data": [
                {
                    **{
                        "_id": str(row["_id"]),
                        "user_id": str(row["user_id"]),
                        "name": row.get("name"),
                        "description": row.get("description"),
                        "icon": str(row.get("icon")),
                        "color": row.get("color"),
                        "created_at": row.get("created_at").isoformat(),
                    },
                    **({"updated_at": row["updated_at"].isoformat()} if "updated_at" in row else {})
                }
                for row in response["data"]
            ]
        }

        return JSONResponse(filter_data, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/category")
@require_auth
async def create_category(request: Request, category: CategoryRequest):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        category = Category(user_id=user_id, name=category.name, description=category.description, icon=category.icon, color=category.color)
        response = category.create()
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/category/{category_id}')
@require_auth
async def get_category_by_id(request: Request, category_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        category = Category()
        response = category.get_by_id(category_id=category_id, user_id= user_id)
        if not response or "data" not in response:
            return JSONResponse(response, status_code=response["status"])
        row = response["data"]
        filter_data = {
            "status": response["status"],
            "message": response["message"],
            "data": 
                {
                    **{
                        "_id": str(row["_id"]),
                        "user_id": str(row["user_id"]),
                        "name": row.get("name"),
                        "description": row.get("description"),
                        "icon": str(row.get("icon")),
                        "color": row.get("color"),
                        "created_at": row.get("created_at").isoformat(),
                    },
                    **({"updated_at": row["updated_at"].isoformat()} if "updated_at" in row else {})
                }
            
        }

        return JSONResponse(filter_data, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/category/{category_id}')
@require_auth
async def update_category(
    request: Request,
    category_id: str = Path(...),
    category_data: Dict[str, Any] = None
):
    
    try:
        session = request.state.session
        user_id = session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized: Session invalid")

        name = category_data.get("name")
        description = category_data.get("description")
        icon = category_data.get("icon")
        color = category_data.get("color")

        category = Category(category_id=category_id, user_id=user_id, name=name, description=description, icon=icon, color=color)
        response = category.update(category_id)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.delete('/category/{category_id}')
@require_auth
async def delete_category(request: Request, category_id: str = Path(...)):
    try:
        session = request.state.session
        user_id = session.get("user_id")
        category = Category()
        response = category.delete(category_id=category_id, user_id=user_id)
        return JSONResponse(response, status_code=response["status"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))