from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.schemas import SampleCreate
from app.services.sample_service import (
    create_sample,
    get_samples,
    get_sample_by_id,
    update_sample,
    delete_sample
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/samples")
def add_sample(sample: SampleCreate, db: Session = Depends(get_db)):
    new_sample = create_sample(db, sample)

    return {
        "message": "Sample saved successfully",
        "id": new_sample.id,
    }


@router.get("/samples")
def read_samples(db: Session = Depends(get_db)):
    return get_samples(db)


@router.get("/samples/{sample_id}")
def read_sample(sample_id: int, db: Session = Depends(get_db)):
    sample = get_sample_by_id(db, sample_id)

    if sample is None:
        raise HTTPException(
            status_code=404,
            detail="Sample not found"
        )

    return sample


@router.put("/samples/{sample_id}")
def edit_sample(
    sample_id: int,
    sample: SampleCreate,
    db: Session = Depends(get_db)
):
    updated_sample = update_sample(db, sample_id, sample)

    if updated_sample is None:
        raise HTTPException(
            status_code=404,
            detail="Sample not found"
        )

    return {
        "message": "Sample updated successfully",
        "id": updated_sample.id,
    }


@router.delete("/samples/{sample_id}")
def remove_sample(sample_id: int, db: Session = Depends(get_db)):
    deleted_sample = delete_sample(db, sample_id)

    if deleted_sample is None:
        raise HTTPException(
            status_code=404,
            detail="Sample not found"
        )

    return {
        "message": "Sample deleted successfully",
        "id": deleted_sample.id,
    }