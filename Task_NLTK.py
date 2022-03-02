import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('treebank')

from nltk.tag import PerceptronTagger
from nltk.corpus import treebank

try:
    your_int = input("Введите число:")
    tagger = PerceptronTagger()
    gold_data = treebank.tagged_sents()[1:int(your_int)]
    print(tagger.accuracy(gold_data))
except ZeroDivisionError:
    print("Вы делите на ноль")
finally:
    print("Всё будет хорошо!!!!!!!")
