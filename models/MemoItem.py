from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

MemoItemBase = declarative_base()


class MemoItem(MemoItemBase):
    __tablename__ = "memo_items"

    id = Column(Integer, Sequence("id"), primary_key=True)
    name = Column(String)
    contents = Column(String)
    type = Column(Integer)

    def __repr__(self):
        return f"MemoItem[id: {self.id}, name: {self.name}, contents: {self.contents}, type: {self.type}]"
