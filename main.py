from words import Words
from ui import UI

COUNT = 20


def program():
    words = Words(file_path='1-1000.csv')
    word_list = words.get_word_list(count=COUNT)
    ui = UI(words=word_list)
    return ui.retry


while True:
    keep_going = program()
    if keep_going == 'No':
        break
