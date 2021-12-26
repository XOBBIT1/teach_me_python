import datetime

def time_of_function(function):
    def wrapped(*args):
        start_time = datetime.datetime.now()
        res = function(*args)
        print(start_time)
        try:
            file = open("day_time_file.txt", 'a', encoding="UTF-8")
            write_file = f"\n Дата:{start_time}\n"
            file.write(write_file)
        except FileNotFoundError:
            file = open("day_time_file.txt", 'w', encoding="UTF-8")
            write_file = f"\n Дата:{start_time}"
            file.write(write_file)
        finally:
            file.close()
        return res
    return wrapped


def compress(string: str) -> str:
    str = " "
    for i in string:
        if i not in str:
            str += f'{i}{string.count(i)}'
    return str

@time_of_function
def compress_decode(string: str):
    str_dec = []
    int_dec = []
    for i in string:
        if i.isdigit():
            int_dec.append(int(i))
        elif i.isalpha():
            str_dec.append(i)
    decode = [el1 * el2 for el1, el2 in zip(str_dec, int_dec)]
    return "".join(decode)

def frequency_sort(items):
    return sorted(items, key= lambda part: -items.count(part))

