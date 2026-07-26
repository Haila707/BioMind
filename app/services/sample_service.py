from sqlalchemy.orm import Session

from app.models.sample import Sample
from app.models.schemas import SampleCreate


def create_sample(db: Session, sample: SampleCreate):
    new_sample = Sample(
        sample_id=sample.sample_id,
        organism=sample.organism,
        tissue=sample.tissue,
        notes=sample.notes,
    )

    db.add(new_sample)
    db.commit()
    db.refresh(new_sample)

    return new_sample


def get_samples(db: Session):
    return db.query(Sample).all()


def get_sample_by_id(db: Session, sample_id: int):
    return db.query(Sample).filter(Sample.id == sample_id).first()


def update_sample(db: Session, sample_id: int, sample_data: SampleCreate):
    sample = db.query(Sample).filter(Sample.id == sample_id).first()

    if sample is None:
        return None

    sample.sample_id = sample_data.sample_id
    sample.organism = sample_data.organism
    sample.tissue = sample_data.tissue
    sample.notes = sample_data.notes

    db.commit()
    db.refresh(sample)

    return sample


def delete_sample(db: Session, sample_id: int):
    sample = db.query(Sample).filter(Sample.id == sample_id).first()

    if sample is None:
        return None

    db.delete(sample)
    db.commit()

    return sample