from sqlalchemy import (Column, Date, Float, ForeignKey, Integer, String, Time,
                        Unicode)

from .database import Base


class CollectionEvents(Base):
    __tablename__ = "collectionevents"
    lotno = Column(String(20), nullable=False, primary_key=True)
    collstartdate = Column(Date)
    collenddate = Column(Date)
    substrate = Column(Unicode(100))
    assocvegetation = Column(Unicode(100))
    habitat = Column(Unicode(100))
    gpslatitude = Column(Float)
    gpslongitude = Column(Float)
    gpsdatum = Column(Unicode(100))
    locality = Column(Unicode(100))
    colllocation = Column(Unicode(400))
    elevation = Column(Float)
    collnotes = Column(Unicode(1400))


class Specimen(Base):
    __tablename__ = "specimens"
    specimenno = Column(String(50), nullable=False, primary_key=True)
    lotno = Column(String(50), ForeignKey("collectionevents.lotno"), nullable=False)
    specimennote = Column(Unicode(500))


class Taxa(Base):
    __tablename__ = "taxa"
    taxno = Column(Integer, nullable=False, primary_key=True)
    taxorder = Column(Unicode(100))
    taxsuborder = Column(Unicode(100))
    taxsuperfamily = Column(Unicode(100))
    taxfamily = Column(Unicode(100))
    taxsubfamily = Column(Unicode(100))
    taxtribe = Column(Unicode(100))
    taxsubtribe = Column(Unicode(100))
    taxgenus = Column(Unicode(100))
    taxsubgenus = Column(Unicode(100))
    taxspecies = Column(Unicode(100))
    taxsubspecies = Column(Unicode(100))
    authority = Column(Unicode(100))
    authorityyear = Column(Unicode(100))


class Determinations(Base):
    __tablename__ = "determinations"
    determinationno = Column(Integer, nullable=False, primary_key=True)
    taxno = Column(Integer, ForeignKey("taxa.taxno"), nullable=False)
    specimenno = Column(String(20), ForeignKey("specimens.specimenno"), nullable=False)
    identifier = Column(Unicode(100))
    iddate = Column(Date)
    verifier = Column(Unicode(100))
    verifierdate = Column(Date)
    idnote = Column(Unicode(1400))


class Images(Base):
    __tablename__ = "images"
    imageno = Column(Integer, primary_key=True)
    specimenno = Column(String(20), ForeignKey("specimens.specimenno"), nullable=False)
    imager = Column(Integer, ForeignKey("actors.actorno"), nullable=False)
    imagedate = Column(Date)
    size = Column(Integer)
    # TODO: figure out how to store images
    imagenotes = Column(Unicode(1400))


class CollectorsForCollectionEvents(Base):
    __tablename__ = "collectorsforcollectionevents"
    collectororder = Column(Integer, primary_key=True)
    lotno = Column(String(20), ForeignKey("collectionevents.lotno"), nullable=False)
    actorno = Column(Integer, ForeignKey("actors.actorno"), nullable=False)


class Actors(Base):
    __tablename__ = "actors"
    actorno = Column(Integer, primary_key=True)
    actorname = Column(Unicode(100))
    actoraffiliation = Column(Unicode(100))
    actornotes = Column(Unicode(1400))
