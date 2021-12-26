import datetime
from Constant import FILE_HANDLERS,INIT_ROW_TEMPLATE



def write_data(handler:str, message: str, mode="a"):
    file = open(FILE_HANDLERS[handler], mode, encoding="UTF-8")
    try:
        file.write(message)
    except IOError:
        print("Ошибка записи лога")
    finally:
        file.close()



def get_num_game() ->int:
    inc = 1
    try:
        file = open(FILE_HANDLERS["GAME_NUM"], "r", encoding="UTF-8")
    except FileNotFoundError:
        write_data("GAME_NUM", str(inc),"w")
        return inc
    try:
        data = file.read()
        if not data:
            return inc
        inc = int(data) + 1
        return inc
    except IOError:
        print("Ошибка Чтения Инкримента")
    finally:
        file.close()
        write_data("GAME_NUM", str(inc), "w")


def write_init(init_data):#
    name = ";".join(i["name"] for i in init_data["users"])
    init_sring = f"\n Номер игры: {init_data['game_num']}\n Режим игры:{init_data['mode']}\n Имя игрока: {name}\n Время игры: {datetime.datetime.now().isoformat()}\n -----------"
    write_data("INIT_GAME", init_sring)

def write_step(user, step, step_num, game_num):
    step_str = "/".join(map(str, step))
    log_string = f"\n Игра под номером {game_num}\n Игрок: {user['name']}\n Ход игрока: {step_num}:{step_str}\n ------------"
    write_data("GAME_STEP", log_string)