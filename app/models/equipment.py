from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Equipment(Base):
    __tablename__ = "equipments"

    code = Column(String, primary_key=True, unique=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    active = Column(Boolean, default=True)
    vessel_code = Column(String, ForeignKey("vessels.code"))

    equipment_owner = relationship("Vessel", back_populates="equipments")
    operations = relationship("Operation", back_populates="operation_owner")
