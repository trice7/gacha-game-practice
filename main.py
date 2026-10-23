import json
from ui import start_menu

with open("data/save.json", 'r', encoding="utf-8") as file:
    saves = json.load(file)

# print(saves)


def main_loop():
    save_exists = True if saves["save_exists"] else False
    start_menu(save_exists, saves)


if __name__ == "__main__":
    main_loop()
