from sqlalchemy import Column, String

from app.db.session import Base


class Vessel(Base):
    __tablename__ = "vessels"

    code = Column(String, primary_key=True, unique=True, index=True)
