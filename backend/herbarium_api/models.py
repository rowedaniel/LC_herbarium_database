from sqlalchemy import (Column, Date, Float, ForeignKey, Integer, String, Time,
                        Unicode)

from .database import Base


class CollectionEvent(Base):
    __tablename__ = "collectionevents"
    lotno = Column(String(50), nullable=False, primary_key=True)
    collector1 = Column(Unicode(200))
    collector2 = Column(Unicode(200))
    collector3 = Column(Unicode(200))
    collector4 = Column(Unicode(200))
    colldate = Column(Date)
    colltime = Column(Time)
    locality = Column(Unicode(200))
    colllocation = Column(Unicode(200))
    collsublocation = Column(Unicode(200))
    collmethod = Column(Unicode(200))
    substrate = Column(Unicode(200))
    assocvegetation = Column(Unicode(200))
    habitat = Column(Unicode(200))
    gpslatitudeverbatim = Column(Unicode(200))
    gpslongitudeverbatim = Column(Unicode(200))
    gpslatitude = Column(Float())
    gpslongitude = Column(Float())
    datum = Column(Unicode(200))
    elevation = Column(Float())
    elevation_units = Column(Unicode(200))
    weathernotes = Column(Unicode(500))
    collnotes = Column(Unicode(500))


class Specimen(Base):
    __tablename__ = "specimens"
    lotno = Column(
        String(50),
        ForeignKey("collectionevents.lotno"),
        nullable=False,
    )
    specimenno = Column(String(50), primary_key=True)
    taxorder = Column(Unicode(200))
    taxsuborder = Column(Unicode(200))
    taxsuperfamily = Column(Unicode(200))
    taxfamily = Column(Unicode(200))
    taxsubfamily = Column(Unicode(200))
    taxtribe = Column(Unicode(200))
    taxsubtribe = Column(Unicode(200))
    taxgenus = Column(Unicode(200))
    taxsubgenus = Column(Unicode(200))
    taxspecies = Column(Unicode(200))
    taxsubspecies = Column(Unicode(200))
    authority = Column(Unicode(200))
    authorityyear = Column(Unicode(200))
    identifier = Column(Unicode(200))
    iddate = Column(Date)
    verifier = Column(Unicode(200))
    verifierdate = Column(Date)
    idnote = Column(Unicode(500))
    specimennote = Column(Unicode(500))
