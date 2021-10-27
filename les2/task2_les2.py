"""
2 Дан зашифрованный текст и набор замен которые использовались для шифрования.
Написать процедуру и вывести на экран расшифрованный текст
"""

text = """@*гда я п^ижимал тебя к г^уди св*ей-
Любви и счастья п*лн и п^ими^ен с судьб*ю-
Я думал: т*льк* сме^ть нас ^азлучит с т*б*ю;
+* в*т ^азлучены мы завистью людей!

Пускай тебя навек- п^елестн*е с*зданье-
&тт*^гла зл*ба их *т се^дца м*ег*;
+*- ве^ь- им не изгнать тв*й *б^аз из нег*-
П*ка не пал тв*й д^уг п*д б^еменем ст^аданья!


И если ме^твецы п^иют п*кинут св*й
И к вечн*й жизни п^ах из тленья в*з^*дится-
&пять чел* м*е на г^удь тв*ю скл*нится:
+ет ^ая для меня- где нет тебя с* мн*й!"""

crypto_keys = (("К", "@",), ("р", "^",), (",", "-"), ("c", "$"), ("О", "&",), ("Н", "+"), ("о", "*"))

text1 = text.replace("@", "К").replace("^", "р").replace("-", ",").replace("$", "c").replace("&", "О").replace("+", "Н").replace("*", "о")
text2 = text.replace(crypto_keys[0][1], crypto_keys[0][0]).replace(crypto_keys[1][1], crypto_keys[1][0]).replace(crypto_keys[2][1], crypto_keys[2][0]).replace(crypto_keys[3][1], crypto_keys[3][0]).replace(crypto_keys[4][1], crypto_keys[4][0]).replace(crypto_keys[5][1], crypto_keys[5][0]).replace(crypto_keys[6][1], crypto_keys[6][0])

print(text1)