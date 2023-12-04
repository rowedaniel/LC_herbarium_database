"""create collectionevents table

Revision ID: 7f18b6b78ba1
Revises:
Create Date: 2023-10-17 10:04:22.528257

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7f18b6b78ba1"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "collectionevents",
        sa.Column("lotno", sa.String(50), nullable=False, primary_key=True),
        sa.Column("collector1", sa.Unicode(200)),
        sa.Column("collector2", sa.Unicode(200)),
        sa.Column("collector3", sa.Unicode(200)),
        sa.Column("collector4", sa.Unicode(200)),
        sa.Column("colldate", sa.Date),
        sa.Column("colltime", sa.Time),
        sa.Column("locality", sa.Unicode(200)),
        sa.Column("colllocation", sa.Unicode(200)),
        sa.Column("collsublocation", sa.Unicode(200)),
        sa.Column("collmethod", sa.Unicode(200)),
        sa.Column("substrate", sa.Unicode(200)),
        sa.Column("assocvegetation", sa.Unicode(200)),
        sa.Column("habitat", sa.Unicode(200)),
        sa.Column("gpslatitudeverbatim", sa.Unicode(200)),
        sa.Column("gpslongitudeverbatim", sa.Unicode(200)),
        sa.Column("gpslatitude", sa.Float()),
        sa.Column("gpslongitude", sa.Float()),
        sa.Column("datum", sa.Unicode(200)),
        sa.Column("elevation", sa.Float()),
        sa.Column("elevation_units", sa.Unicode(200)),
        sa.Column("weathernotes", sa.Unicode(500)),
        sa.Column("collnotes", sa.Unicode(500)),
    )


def downgrade() -> None:
    op.drop_table("collectionevents")
