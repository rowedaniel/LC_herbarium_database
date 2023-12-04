from typing import Generator

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from . import models, schemas
from .crud import (create_collectionevent, create_specimen,
                   get_collectionevent_one_or_none, get_collectionevents,
                   get_specimen_one_or_none, get_specimens)
from .database import SessionLocal

app = FastAPI(default_response_class=ORJSONResponse)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/collectionevents/by_id", response_model=schemas.CollectionEvent)
async def coll_event_by_id(
    item_id: int, db: Session = Depends(get_db)
) -> schemas.CollectionEvent:
    res = get_collectionevent_one_or_none(db, item_id)
    if res is None:
        raise HTTPException(status_code=404, detail="item not found")
    return res


@app.get("/collectionevents/all", response_model=list[schemas.CollectionEvent])
async def all_coll_events(
    offset: int = 0, db: Session = Depends(get_db)
) -> list[schemas.CollectionEvent]:
    res = get_collectionevents(db, offset)
    return res


@app.post("/collectionevents/create", response_model=schemas.CollectionEvent)
async def create_new_coll_event(
    item: schemas.CollectionEventCreate, db: Session = Depends(get_db)
) -> schemas.CollectionEvent:
    res = create_collectionevent(db, item)
    return res


@app.get("/specimens/by_id", response_model=schemas.Specimen)
async def specimen_by_id(item_id: int, db: Session = Depends(get_db)) -> schemas.Specimen:
    res = get_specimen_one_or_none(db, item_id)
    if res is None:
        raise HTTPException(status_code=404, detail="item not found")
    return res


@app.get("/specimens/all", response_model=list[schemas.Specimen])
async def all_specimens(
    offset: int = 0, db: Session = Depends(get_db)
) -> list[schemas.Specimen]:
    res = get_specimens(db, offset)
    return res


@app.post("/specimens/create", response_model=schemas.Specimen)
async def create_new_specimen(
    item: schemas.SpecimenCreate, db: Session = Depends(get_db)
) -> schemas.Specimen | None:
    res = create_specimen(db, item)
    return res
