from sqlalchemy import Column, Integer, String
from app.database.database import Base


class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)
    sample_id = Column(String, unique=True, index=True)
    organism = Column(String)
    tissue = Column(String)
    notes = Column(String, nullable=True)