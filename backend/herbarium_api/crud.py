from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from typing import Type

from . import models, schemas

QUERY_LIMIT = 100


def get_collectionevent_one_or_none(
    db: Session, item_id: int
) -> schemas.CollectionEvent | None:
    return (
        db.query(models.CollectionEvent)
        .filter(models.CollectionEvent.id == item_id)
        .one_or_none()
    )


def get_collectionevents(db: Session, offset: int = 0) -> list[schemas.CollectionEvent]:
    return (
        db.query(models.CollectionEvent)
        .offset(offset * QUERY_LIMIT)
        .limit(QUERY_LIMIT)
        .all()
    )


def create_collectionevent(
    db: Session, item: schemas.CollectionEventCreate
) -> schemas.CollectionEvent:
    collectionevent = models.CollectionEvent(**item.dict())
    db.add(collectionevent)
    db.commit()
    db.refresh(collectionevent)

    return collectionevent


def get_specimen_one_or_none(db: Session, item_id: int) -> schemas.Specimen | None:
    return db.query(models.Specimen).filter(models.Specimen.id == item_id).one_or_none()


def get_specimens(db: Session, offset: int = 0) -> list[schemas.Specimen]:
    return list(
        db.query(models.Specimen).offset(offset * QUERY_LIMIT).limit(QUERY_LIMIT).all()
    )


def create_specimen(db: Session, item: schemas.SpecimenCreate) -> schemas.Specimen:
    specimen = models.Specimen(**item.dict())
    db.add(specimen)
    db.commit()
    db.refresh(specimen)

    return schemas.Specimen.from_orm(specimen)
