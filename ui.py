import ttkbootstrap as ttk
from ttkbootstrap.dialogs.dialogs import Messagebox
import time

BG = '#343A40'
FG_RIGHT = '#006633'
FG_WRONG = '#990000'


class UI:

    def __init__(self, words):
        self.window = ttk.Window()
        self.window.title("SpeedTest")
        self.window.config(padx=100, pady=50, background=BG)
        self.window.geometry("860x280")
        self.retry = "No"
        self.wpm_now = None
        self.i = 0
        self.j = 1
        self.word_dict = {}
        self.entry_dict = {}
        self.num = 1
        for word in words:
            if self.i > 4:
                self.j += 1
                self.i = 0
            self.w = ttk.Label(bootstyle='inverse-dark', font=('Helvetica bold', 20), text=word)
            self.w.grid(row=self.j, column=self.i)
            self.i += 1
            self.word_dict.update({self.num: word})
            self.entry_dict.update({self.num: self.w})
            self.num += 1
        self.word_iter_list = iter(self.word_dict)
        self.entry = ttk.Entry(width=60, bootstyle="danger", font=('Helvetica bold', 15))
        self.entry.bind('<Return>', lambda event: self.next())
        self.entry.bind('<space>', lambda event: self.next())
        self.entry.grid(row=5, column=0, columnspan=5)
        self.t0 = time.time()
        self.wpm = ttk.Label(text='WPM : 0', bootstyle='inverse-secondary', font=('Helvetica bold', 20))
        self.wpm.grid(row=0, column=2)
        self.window.mainloop()

    def next(self):
        t1 = time.time()
        time_taken = (t1 - self.t0) / 60
        user_entry = self.entry.get()
        self.entry.delete(0, 100)
        try:
            key = next(self.word_iter_list)
        except StopIteration:
            self.retry = Messagebox.show_question(f'WPM: {self.wpm_now :.2f}\nWould you like to try again?', title='End of words!', alert=False,
                                                  buttons=['No:secondary', 'Yes:primary'])
            self.window.destroy()
        else:
            self.wpm_now = key / time_taken
            self.wpm.config(text=f'WPM : {self.wpm_now:.2f}')
            if str(user_entry.replace(" ", "")) == self.word_dict.get(key):
                foreground = FG_RIGHT
            else:
                foreground = FG_WRONG
            self.entry_dict.get(key).config(foreground=foreground)
