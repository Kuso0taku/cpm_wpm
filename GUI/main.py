from time import time
from random import choice as ch
import tkinter as tk

class App:
    def __init__(self):
        with open('../text.txt', 'r', encoding='UTF-8') as f:
            self.text = ch(f.readlines())
        for chars in [['ё', 'е'], ['Ё', 'е'], ['«', '"'], ['»', '"']]:
            self.text.replace(chars[0], chars[1])

        self.startTime = self.endTime = self.start = self.wrong = self.characters = self.words = self.cpm = self.wpm = self.accuracy = self.cpmWpm = 0


        self.root = tk.Tk()
        root = self.root

        self.main_frm = tk.Frame(root, bg='#0d0124', width=550, height=350)
        main_frm = self.main_frm
        self.frm = tk.Frame(root, bg='#0b1f07', width=550, height=350)
        frm = self.frm

        self.lbl = tk.Label(main_frm, text='Начните печатать текст, чтобы начать', font=('Comic', 20), fg='green',
                            bg='#0d0124')
        self.ent = tk.Entry(main_frm, textvariable=True, font=('Arial', 20), width=25, state='normal', fg='purple',
                            bg='#0d0124')
        self.ent.insert(0, self.text)
        self.btn = tk.Button(main_frm, command=self.cpm_wpm, text='Завершить', font=('Times New Roman', 15), fg='green',
                        bg='#0d0124')
        self.lbl_end = tk.Label(frm,
                                text=f'Твой результат: \ncpm: {self.cpm}\nwpm: {self.wpm}\nточность: {self.accuracy}%',
                                font=('Sans', 30), fg='purple', bg='#0b1f07', width=22)
        self.again = tk.Button(frm, command=self.Again, text='Еще раз', font=('Times New Roman', 15), fg='yellow',
                               bg='#0b1f07', width=7)
        self.quit = tk.Button(frm, command=self.Quit, text='Выйти', font=('Times New Roman', 15), fg='red',
                              bg='#0b1f07', width=7)


    def Window(self):
        root = self.root
        root['bg'] = 'black'
        root.title('cpm_wpm')
        #root.geometry('550x350')
        #root.resizable(width=False, height=False)
        root.bind('<Key>', self.keyboard)

        root.mainloop()

    def Main_Frame(self):
        self.lbl.pack(padx=10, pady=50)
        self.ent.pack(padx=10, pady=10)
        self.btn.pack(pady=50)
        self.main_frm.grid()

    def Frame(self):
        frm = self.frm
        self.lbl_end.pack(pady=10)
        self.again.pack(pady=10)
        self.quit.pack(pady=10)
        frm.grid()

    def Text(self):
        with open('../text.txt', 'r', encoding='UTF-8') as f:
            self.text = ch(f.readlines())
        for chars in [['ё', 'е'], ['Ё', 'е'], ['«', '"'], ['»', '"']]:
            self.text.replace(chars[0], chars[1])
        self.ent.delete(0, 'end')
        self.ent.insert(0, self.text)

    def Again(self):
        self.startTime = self.endTime = self.start = self.wrong = self.characters = self.words = self.cpm = self.wpm = self.accuracy = self.cpmWpm = 0

        self.frm.grid_forget()
        self.main_frm.grid()

        self.Text()

        self.cpmWpm = 0

    def Quit(self):
        self.root.quit()

    def cpm_wpm(self):
        self.endTime = round(time())
        endTime = self.endTime
        startTime = self.startTime

        root = self.root


        inputTime = (endTime - startTime)

        characters = self.characters
        words = self.words
        wrong = self.wrong


        minLen = min(characters, len(self.text))
        try:
            cpm = round(characters / inputTime * 60)
            wpm = round(words / inputTime * 60)
            accuracy = 100 - round(wrong / minLen * 100)
        except ZeroDivisionError:
            cpm = 0
            wpm = 0
            accuracy = 0


        self.main_frm.grid_forget()
        self.cpm, self.wpm, self.accuracy = cpm, wpm, accuracy
        self.lbl_end.configure(text=f'Твой результат: \ncpm: {self.cpm}\nwpm: {self.wpm}\nточность: {self.accuracy}%')
        self.Frame()

        self.cpmWpm = 1

    def keyboard(self, event):
        root = self.root
        if event.keysym == 'Escape':
            root.quit()
        elif event.keysym == 'Return':
            if self.cpmWpm == 0:
                self.cpmWpm = 1
                self.cpm_wpm()
            else:
                self.Again()
        try:
            if len(self.ent.get()) == 0:
                self.cpm_wpm()
        except:
            pass
        else:
            if event.char == self.ent.get()[0]:
                if self.start == 0:
                    self.startTime = round(time())
                    self.start = 1
                self.characters += 1
                if event.char == ' ':
                    self.words += 1
                self.ent.delete(0, 1)
            else:
                if self.start == 1:
                    self.wrong += 1

    def main(self):
        self.Main_Frame()
        self.Window()


if __name__ == '__main__':
    App().main()
