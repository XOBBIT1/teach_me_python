def log_errors(func):
    def surrogate(*args, **kwargs):
        result = func(*args, **kwargs)
        file = open("text.txt", mode='a')
        file_content = "Тут будет результат"
        file.write(f"Тут будет результат:\n {result}\n")
        return result

    return surrogate


# Проверить работу на следующих функциях
@log_errors
def perky(a,b):
    return a+b

res = perky(1,2)
print(res)