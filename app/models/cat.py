from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import Optional

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]
    pet_count: Mapped[Optional[int]]
    caretaker_id: Mapped[Optional[int]] = mapped_column(ForeignKey("caretaker.id"))
    caretaker: Mapped[Optional["Caretaker"]] = relationship(back_populates="cats")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "personality": self.personality,
            "pet_count": self.pet_count if self.pet_count else 0,
            "caretaker": self.caretaker.name if self.caretaker_id else None
        }

    @classmethod
    def from_dict(cls, cat_data):
        return cls(
            name=cat_data["name"],
            color=cat_data["color"],
            personality=cat_data["personality"],
            pet_count=cat_data.get("pet_count", 0),
            caretaker_id=cat_data.get("caretaker_id", None)
        )