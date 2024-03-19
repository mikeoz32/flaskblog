from datetime import datetime
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, validates
from flaskblog.model.base import CreatedAtMixin, IDMixin, db
from email_validator import validate_email


class User(IDMixin, CreatedAtMixin, db.Model):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    @validates("email")
    def validate_email(self, key, value):
        return validate_email(value, check_deliverability=False).normalized
