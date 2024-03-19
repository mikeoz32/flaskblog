
from typing import Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from flaskblog.model.base import CreatedAtMixin, IDMixin, db


class Comment(IDMixin, CreatedAtMixin, db.Model):
    content: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
