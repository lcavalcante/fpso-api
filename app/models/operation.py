from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    type = Column(String, index=True)
    cost = Column(String)
    code = Column(String, ForeignKey("equipments.code"))

    operation_owner = relationship("Equipment", back_populates="operations")
