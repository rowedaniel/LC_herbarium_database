import csv
from datetime import date, time

from herbarium_api.crud import create_collectionevent, create_specimen
from herbarium_api.database import SessionLocal
from herbarium_api.schemas import CollectionEventCreate, SpecimenCreate


def convert_date(date_str: str) -> date | None:
    if date_str == "":
        return None
    else:
        return date.fromisoformat(date_str)


def convert_time(time_str: str) -> time | None:
    if time_str == "":
        return None
    else:
        return time.fromisoformat(time_str)


def send_coll_data_to_database(filename: str):
    db = SessionLocal()
    with open(filename, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')

        # skip header rows
        spamreader.__next__()
        spamreader.__next__()

        for row in spamreader:
            if "".join(row).strip() == "":
                continue

            col = CollectionEventCreate(
                lotno=row[0],
                collector1=row[1],
                collector2=row[2],
                collector3=row[3],
                collector4=row[4],
                colldate=convert_date(row[5]),
                colltime=convert_time(row[6]),
                locality=row[7],
                colllocation=row[8],
                collsublocation=row[9],
                collmethod=row[10],
                substrate=row[11],
                assocvegetation=row[12],
                habitat=row[13],
                gpslatitudeverbatim=row[14],
                gpslongitudeverbatim=row[15],
                gpslatitude=row[16],
                gpslongitude=row[17],
                datum=row[18],
                elevation=row[19],
                elevation_units=row[20],
                weathernotes=row[21],
                collnotes=row[22],
            )

            create_collectionevent(db, col)

    db.close()


def send_specimen_data_to_database(filename: str):
    db = SessionLocal()
    with open(filename, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')

        # skip header rows
        spamreader.__next__()
        spamreader.__next__()

        for row in spamreader:
            if "".join(row).strip() == "":
                continue

            col = SpecimenCreate(
                lotno=row[0],
                specimenno=row[1],
                taxorder=row[2],
                taxsuborder=row[3],
                taxsuperfamily=row[4],
                taxfamily=row[5],
                taxsubfamily=row[6],
                taxtribe=row[7],
                taxsubtribe=row[8],
                taxgenus=row[9],
                taxsubgenus=row[10],
                taxspecies=row[11],
                taxsubspecies=row[12],
                authority=row[13],
                authorityyear=row[14],
                identifier=row[15],
                iddate=convert_date(row[16]),
                verifier=row[17],
                verifierdate=convert_date(row[18]),
                idnote=row[19],
                specimennote=row[20],
            )

            create_specimen(db, col)


if __name__ == "__main__":
    import sys

    coll_filename = sys.argv[1]
    spec_filename = sys.argv[2]
    send_coll_data_to_database(coll_filename)
    send_specimen_data_to_database(spec_filename)
