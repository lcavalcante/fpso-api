from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Vessel(Base):
    __tablename__ = "vessels"

    code = Column(String, primary_key=True, unique=True, index=True)

    equipments = relationship("Equipment", back_populates="equipment_owner")
