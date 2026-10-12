import json
from ui import start_menu

with open("data/save.json", 'r', encoding="utf-8") as file:
    saves = json.load(file)

# print(saves)


def main_loop():
    previous_data = True if saves["save_exists"] else False
    start_menu(previous_data, saves)


if __name__ == "__main__":
    main_loop()
