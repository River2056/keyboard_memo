from sqlalchemy import create_engine

from models.MemoItem import MemoItemBase
from models.MemoType import TypeBase

def main():
    engine = create_engine("sqlite:///memo.db", echo=False)

    MemoItemBase.metadata.create_all(engine)
    TypeBase.metadata.create_all(engine)
    

if __name__ == "__main__":
    main()
