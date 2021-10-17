"""2
До конца не получается, пока сложно
"""

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def my_func(input_string):
    a = input_string.lower()
    b = dict(zip(MORSE.values(), MORSE.keys()))
    c = list(map(lambda n: b[n], a))
    d = " ".join(c)
    return d



def my_func2(encoded_string):
    a = encoded_string.split()
    b = list(map(lambda n: MORSE[n], a))
    b[0] = b[0].upper()
    c = "".join(b)
    return c


print(my_func2(my_func(input('Введите текст для шифрования :'))))