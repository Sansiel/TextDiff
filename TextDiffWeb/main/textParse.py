from langdetect import detect
import nltk
from nltk.stem import WordNetLemmatizer


class TextToDiff:
    def __init__(self):
        pass

    @staticmethod
    def parse(text):
        if detect(text) == 'en':
            return True
        else:
            return False

    @staticmethod
    def diff(text, summary_dict):
        text = str(text).lower()  # Данные
        punctuations = "?:!.,;"
        words = 0
        summary = 0
        max_difficult = 0
        if summary_dict is None:  # Для тестирований
            summary_dict = TextToDiff.get_summary_dict()

        sentence_words = nltk.word_tokenize(text)  # Морфологический анализ
        for word in sentence_words:
            if word in punctuations:
                sentence_words.remove(word)
        word_net_lemma = WordNetLemmatizer()
        word_list = [word_net_lemma.lemmatize(x, pos="v") for x in sentence_words]
        # print(word_list)

        lemmas = set([x for x in word_list if x.isalpha() and x in summary_dict])  # Убираем бессмысленость в тексте
        for lemma in lemmas:
            summary += summary_dict[lemma]
            if summary_dict[lemma] > max_difficult:
                max_difficult = summary_dict[lemma]
            words += 1
        # print(lemmas)  # Tests
        # print(summary, words, max_difficult)  # Tests

        x = 5 * (summary / words / max_difficult)
        # print(x)  # Tests
        x = round(x, 2)
        # print(x)  # Tests
        return x

    @staticmethod
    def get_summary_dict():
        inp = open('.//main//en_dict.txt', encoding='utf-8')
        # inp = open('.//main//lemmas.txt', encoding='utf-8')
        summary_dict = {}
        for line in inp:
            line_list = line.split(' ')
            line_list[1] = float(line_list[1])
            summary_dict[line_list[0]] = line_list[1]
        inp.close()
        return summary_dict
