import nltk # импортируем библиотеку
nltk.download('averaged_perceptron_tagger')# устанавливаем пакеты
nltk.download('treebank')# устанавливаем пакеты

from nltk.tag import PerceptronTagger# из библиотеки nltk папку tag мы забираем табличку с файлами PerceptronTagger
from nltk.corpus import treebank# из библиотеки nltk папку corpus, из этой папки мы функцию, которая считывает фалы PerceptronTagge

tagger = PerceptronTagger()# присваиваем переменной фалы
gold_data = treebank.tagged_sents()[1:10]# заносим в них данные для подщёта
print(tagger.accuracy(gold_data))# выводим


