from sqlalchemy import Column, Integer, String
from app.database.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    description = Column(String)
    role = Column(String)

    status = Column(String, default="active")

    capabilities = Column(String)