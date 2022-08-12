from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

TypeBase = declarative_base()


class MemoType(TypeBase):
    __tablename__ = "memo_types"

    id = Column(Integer, Sequence("id"), primary_key=True)
    memo_type = Column(String)

    def __repr__(self):
        return f"MemoItem[id: {self.id}, memo_type: {self.memo_type}]"
