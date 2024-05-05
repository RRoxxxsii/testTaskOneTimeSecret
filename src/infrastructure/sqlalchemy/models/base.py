import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]  # noqa


class AbstractModel(DeclarativeBase):
    _repr_cols_num: int = 3
    _repr_cols: tuple = tuple()

    id: Mapped[intpk]

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self._repr_cols or idx < self._repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__} {', '.join(cols)}>"


time_created = Annotated[
    datetime.datetime,
    mapped_column(DateTime(timezone=True), server_default=func.now()),
]
