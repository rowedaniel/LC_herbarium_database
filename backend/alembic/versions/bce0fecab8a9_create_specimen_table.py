"""create specimen table

Revision ID: bce0fecab8a9
Revises: 7f18b6b78ba1
Create Date: 2023-10-26 20:18:32.757126

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "bce0fecab8a9"
down_revision: Union[str, None] = "7f18b6b78ba1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "specimens",
        sa.Column(
            "lotno",
            sa.String(50),
            sa.ForeignKey("collectionevents.lotno"),
            nullable=False,
        ),
        sa.Column("specimenno", sa.String(50), nullable=False, primary_key=True),
        sa.Column("taxorder", sa.Unicode(200)),
        sa.Column("taxsuborder", sa.Unicode(200)),
        sa.Column("taxsuperfamily", sa.Unicode(200)),
        sa.Column("taxfamily", sa.Unicode(200)),
        sa.Column("taxsubfamily", sa.Unicode(200)),
        sa.Column("taxtribe", sa.Unicode(200)),
        sa.Column("taxsubtribe", sa.Unicode(200)),
        sa.Column("taxgenus", sa.Unicode(200)),
        sa.Column("taxsubgenus", sa.Unicode(200)),
        sa.Column("taxspecies", sa.Unicode(200)),
        sa.Column("taxsubspecies", sa.Unicode(200)),
        sa.Column("authority", sa.Unicode(200)),
        sa.Column("authorityyear", sa.Unicode(200)),
        sa.Column("identifier", sa.Unicode(200)),
        sa.Column("iddate", sa.Date),
        sa.Column("verifier", sa.Unicode(200)),
        sa.Column("verifierdate", sa.Date),
        sa.Column("idnote", sa.Unicode(500)),
        sa.Column("specimennote", sa.Unicode(500)),
    )



def downgrade() -> None:
    op.drop_table("specimens")
