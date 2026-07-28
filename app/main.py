from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.api.samples import router as samples_router
from app.api.users import router as users_router
from app.api.agents import router as agents_router
from app.api.orchestrator import router as orchestrator_router

from app.database.database import engine, Base
from app.models.sample import Sample
from app.models.user import User
from app.models.agent import Agent


# إنشاء الجداول
Base.metadata.create_all(bind=engine)


# تحديث جدول agents الموجود بدون حذف البيانات
with engine.connect() as connection:

    try:
        connection.execute(
            text(
                "ALTER TABLE agents ADD COLUMN status VARCHAR DEFAULT 'active'"
            )
        )
        connection.commit()

    except Exception:
        pass


    try:
        connection.execute(
            text(
                "ALTER TABLE agents ADD COLUMN capabilities VARCHAR"
            )
        )
        connection.commit()

    except Exception:
        pass



app = FastAPI(
    title="BioMind",
    description="AI Scientific Decision Support Platform",
    version="1.0.0"
)



# السماح للـ Frontend بالاتصال بالـ Backend
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://bio-mind.vercel.app",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)



# Routers
app.include_router(samples_router)
app.include_router(users_router)
app.include_router(agents_router)
app.include_router(orchestrator_router)



@app.get("/")
def home():

    return {
        "message": "BioMind is running",
        "status": "active"
    }