import random

FILESIZE = 1000  # size of the file


class Words:

    def __init__(self, file_path):
        self.word_list = []
        self.file = file_path

    def get_word(self):
        offset = random.randrange(FILESIZE)
        with open(self.file) as f:
            f.seek(offset)
            f.readline()
            word = f.readline()
            if len(word) == 0:
                f.seek(0)
                word = f.readline()
            return word

    def get_word_list(self, count):
        for _ in range(0, count):
            word = self.get_word().replace('\n', '').replace('"', '')
            self.word_list.append(word)
        return self.word_list
