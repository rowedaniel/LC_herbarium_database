from datetime import time, date

from pydantic import BaseModel, constr


class CollectionEventBase(BaseModel):
    lotno: constr(max_length=50)
    collector1: constr(max_length=200)
    collector2: constr(max_length=200)
    collector3: constr(max_length=200)
    collector4: constr(max_length=200)
    colldate: date|None
    colltime: time|None
    locality: constr(max_length=200)
    colllocation: constr(max_length=200)
    collsublocation: constr(max_length=200)
    collmethod: constr(max_length=200)
    substrate: constr(max_length=200)
    assocvegetation: constr(max_length=200)
    habitat: constr(max_length=200)
    gpslatitudeverbatim: constr(max_length=200)
    gpslongitudeverbatim: constr(max_length=200)
    gpslatitude: float|None
    gpslongitude: float|None
    datum: constr(max_length=200)
    elevation: float|None
    elevation_units: constr(max_length=200)
    weathernotes: constr(max_length=500)
    collnotes: constr(max_length=500)


class CollectionEventCreate(CollectionEventBase):
    pass


class CollectionEvent(CollectionEventBase):

    class Config:
        from_attributes = True


class SpecimenBase(BaseModel):
    lotno: constr(max_length=50)
    specimenno: constr(max_length=50)
    taxorder: constr(max_length=200)
    taxsuborder: constr(max_length=200)
    taxsuperfamily: constr(max_length=200)
    taxfamily: constr(max_length=200)
    taxsubfamily: constr(max_length=200)
    taxtribe: constr(max_length=200)
    taxsubtribe: constr(max_length=200)
    taxgenus: constr(max_length=200)
    taxsubgenus: constr(max_length=200)
    taxspecies: constr(max_length=200)
    taxsubspecies: constr(max_length=200)
    authority: constr(max_length=200)
    authorityyear: constr(max_length=200)
    identifier: constr(max_length=200)
    iddate: date|None
    verifier: constr(max_length=200)
    verifierdate: date|None
    idnote: constr(max_length=500)
    specimennote: constr(max_length=500)

class SpecimenCreate(SpecimenBase):
    pass


class Specimen(SpecimenBase):

    class Config:
        from_attributes = True
