import sqlite3


class dictionary_work():

    def __init__(self):
        dictionary_work.data_upload()

    @staticmethod
    def get_dict():
        inp = open('.//main//en_dict.txt', encoding='utf-8')
        # inp = open('.//main//lemmas.txt', encoding='utf-8')
        summary_dict = {}
        for line in inp:
            line_list = line.split(' ')
            line_list[1] = float(line_list[1])
            summary_dict[line_list[0]] = line_list[1]
        inp.close()
        return summary_dict

    @staticmethod
    def data_upload():
        conn = sqlite3.connect('dictionary.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", dictionary_work.get_dict())
        conn.commit()