from typing import Text
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from flaskblog.model.base import CreatedAtMixin, IDMixin, db

class Post(IDMixin, CreatedAtMixin, db.Model):
    __tablename__ = "posts"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title:Mapped[str] = mapped_column(String, unique=True, nullable=False)
    content:Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
