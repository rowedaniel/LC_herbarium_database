from datetime import date, time

from pydantic import BaseModel, constr


class CollectionEventsBase(BaseModel):
    lotno: constr(max_length=20)
    collstartdate: date
    collenddate: date
    substrate: constr(max_length=100)
    assocvegetation: constr(max_length=100)
    habitat: constr(max_length=100)
    gpslatitude: float
    gpslongitude: float
    gpsdatum: constr(max_length=100)
    locality: constr(max_length=100)
    colllocation: constr(max_length=400)
    elevation: float
    collnotes: constr(max_length=1400)


class CollectionEventsCreate(CollectionEventsBase):
    pass


class CollectionEvents(CollectionEventsBase):
    class Config:
        from_attributes: True


class SpecimenBase(BaseModel):
    specimenno: constr(max_length=50)
    lotno: constr(max_length=50)
    specimennote: constr(max_length=500)


class SpecimenCreate(SpecimenBase):
    pass


class Specimen(SpecimenBase):
    class Config:
        from_attributes: True


class TaxaBase(Base):
    taxno: int
    taxorder: constr(max_length=100)
    taxsuborder: constr(max_length=100)
    taxsuperfamily: constr(max_length=100)
    taxfamily: constr(max_length=100)
    taxsubfamily: constr(max_length=100)
    taxtribe: constr(max_length=100)
    taxsubtribe: constr(max_length=100)
    taxgenus: constr(max_length=100)
    taxsubgenus: constr(max_length=100)
    taxspecies: constr(max_length=100)
    taxsubspecies: constr(max_length=100)
    authority: constr(max_length=100)
    authorityyear: constr(max_length=100)


class TaxaCreate(TaxaBase):
    pass


class Taxa(TaxaBase):
    class Config:
        from_attributes: True


class DeterminationsBase(BaseModel):
    determinationno: int
    taxno: int
    specimenno: constr(max_length=20)
    identifier: constr(max_length=100)
    iddate: date
    verifier: constr(max_length=100)
    verifierdate: date
    idnote: constr(max_length=1400)


class DeterminationsCreate(DeterminationsBase):
    pass


class Determinations(DeterminationsBase):
    class Config:
        from_attributes: True


class ImagesBase(BaseModel):
    imageno: int
    specimenno: constr(max_length=20)
    imager: int
    imagedate: date
    size: int
    # TODO: inputting images
    imagenotes: constr(max_length=1400)


class ImagesCreate(ImagesBase):
    pass


class Images(ImagesBase):
    class Config:
        from_attributes: True


class CollectorsForCollectionEventsBase(Base):
    collectororder: int
    lotno: constr(max_length=20)
    actorno: int


class CollectorsForCollectionEventsCreate(CollectorsForCollectionEventsBase):
    pass


class CollectorsForCollectionEvents(CollectorsForCollectionEventsBase):
    class Config:
        from_attributes: True


class ActorsBase(Base):
    __tablename__: "actors"
    actorno: int
    actorname: constr(max_length=100)
    actoraffiliation: constr(max_length=100)
    actornotes: constr(max_length=1400)


class ActorsCreate(ActorsBase):
    pass


class Actors(ActorsBase):
    class Config:
        from_attributes: True
