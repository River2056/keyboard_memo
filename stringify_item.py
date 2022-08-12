import json
import pyperclip


def main():
    item = {"account": "tifa2056", "password": "kevin2056", "trade_num": "0625"}
    jsonify = json.dumps(item)

    print(jsonify)
    pyperclip.copy(jsonify)


if __name__ == "__main__":
    main()
