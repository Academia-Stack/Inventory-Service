from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum

from service.dbConnection import db

class ItemType(enum.Enum):
    LAPTOP = "LAPTOP"
    HEADPHONE = "HEADPHONE"
    MOUSE = "MOUSE"
    SPEAKER = "SPEAKER"
    WEBCAM = "WEBCAM"

class AssigneeType(enum.Enum):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"

class InventoryItem(db.Model):
    __tablename__ = "inventory_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    type = Column(Enum(ItemType), nullable=False)
    model_name = Column(String, nullable=False)

    assigned_to = Column(UUID(as_uuid=True), nullable=True)
    assignee_type = Column(Enum(AssigneeType), nullable=True)