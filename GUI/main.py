from time import time
from random import choice as ch
import tkinter as tk

class App:
    def __init__(self):
        with open('../text.txt', 'r', encoding='UTF-8') as f:
            self.text = ch(f.readlines())
        for chars in [['ё', 'е'], ['Ё', 'е'], ['«', '"'], ['»', '"']]:
            self.text.replace(chars[0], chars[1])

        self.startTime = 0
        self.endTime = 0
        self.start = 0
        self.wrong = 0
        self.characters = 0
        self.words = 0

        self.root = tk.Tk()
        root = self.root

        self.lbl = tk.Label(root, text='Начните печатать текст, чтобы начать', font=('Comic', 20), fg='green', bg='#0d0124')
        self.ent = tk.Entry(root, textvariable=True, font=('Arial', 20), width=75, state='normal', fg='purple', bg='#0d0124')
        self.ent.insert(0, self.text)
        self.btn = tk.Button(root, command=self.cpm_wpm, text='Завершить', font=('Times New Roman', 15), fg='green',
                        bg='#0d0124')

    def Window(self):
        root = self.root
        root['bg'] = '#0d0124'
        root.title('cpm_wpm')
        root.geometry('550x350')
        # root.resizable(width=False, height=False)
        root.bind('<Key>', self.keyboard)

        root.mainloop()

    def Pack(self):
        self.lbl.pack(padx=10, pady=50)
        self.ent.pack(padx=10, pady=10)
        self.btn.pack(pady=50)

    def cpm_wpm(self):
        self.endTime = round(time())
        endTime = self.endTime
        startTime = self.startTime

        root = self.root
        self.lbl.destroy()
        self.ent.destroy()
        self.btn.destroy()


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

        tk.Label(root, text=f'Твой результат: \ncpm: {cpm}\nwpm: {wpm}\nточность: {accuracy}%', font=('Sans', 30), fg='purple', bg='#0d0124').pack(expand=True)

    def keyboard(self, event):
        root = self.root
        if event.keysym == 'Escape':
            root.quit()
        elif event.keysym == 'Return':
            self.cpm_wpm()
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
        self.Pack()
        self.Window()


if __name__ == '__main__':
    App().main()
