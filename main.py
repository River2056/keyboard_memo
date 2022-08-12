import sys
import json
import pyperclip
from sqlalchemy import create_engine

from models.MemoItem import MemoItemBase
from models.MemoType import TypeBase


def process_row(item):
    item_values = [
        (idx, value) for idx, value in enumerate(json.loads(item[2]).values())  # type: ignore
    ]

    print()
    print("choose value to copy: ")
    for idx, value in item_values:
        print(f"{idx + 1}: {value}")

    choose_idx = int(input()) - 1
    value = list(filter(lambda x: x[0] == choose_idx, item_values))[0][1]
    print(f"{value} copied to clipboard")
    pyperclip.copy(value)


def main():
    engine = create_engine("sqlite:///memo.db", echo=False)

    MemoItemBase.metadata.create_all(engine)
    TypeBase.metadata.create_all(engine)

    while True:
        keyword = input("enter name or blank for list options...")

        if not keyword:
            all_data = []
            with engine.connect() as con:
                rs = con.execute("select * from memo_items")

                for row in rs:
                    all_data.append(row)

            print("choose data")
            for idx, data in enumerate(all_data):
                print(f"{idx + 1}. {data[1]}")

            choose_idx = int(input()) - 1

            item = all_data[choose_idx]
            process_row(item)

        else:
            with engine.connect() as con:
                rs = con.execute(f"select * from memo_items where name like '%{keyword}%'")
                item = rs.first()
                if item:
                    process_row(item)
                else:
                    # search through types
                    rs = con.execute(
                        f"select * from memo_types where memo_type = '{keyword}'"
                    )
                    item = rs.first()
                    if item:
                        process_row(item)
                    else:
                        print("your keyword isn't found in database")


if __name__ == "__main__":
    main()
