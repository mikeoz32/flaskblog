from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, func

class Base(DeclarativeBase):
    ...

db = SQLAlchemy(model_class=Base)
alembic = Alembic()

def init_models(app: Flask):
    db.init_app(app)
    alembic.init_app(app)


class IDMixin():
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

class CreatedAtMixin():
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
