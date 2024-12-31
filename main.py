from fastapi import FastAPI
from .routes.user_route import router as user_routes
from .routes.category_route import router as category_routes
from .routes.notes_route import router as notes_routes
from .routes.todo_route import router as todo_routes
from .routes.agenda_route import router as agenda_routes
from .routes.schedule_route import router as schedule_routes

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(user_routes, prefix="/api/v1", tags=["Auth"])
app.include_router(category_routes, prefix="/api/v1", tags=["Category"])
app.include_router(notes_routes, prefix="/api/v1", tags=["Notes"])
app.include_router(todo_routes, prefix="/api/v1", tags=["ToDo"])
app.include_router(agenda_routes, prefix="/api/v1", tags=["Agenda"])
app.include_router(schedule_routes, prefix="/api/v1", tags=["Schedule"])
