from time import time, sleep
from random import choice as ch

def cpm_wpm():
    with open('../text.txt', 'r', encoding='UTF-8') as f:
        text = ch(f.readlines())
    for chars in [['ё', 'е'], ['Ё', 'е'], ['«', '"'], ['»', '"']]:
        text.replace(chars[0], chars[1])

    print(f'You need to enter this text:\n{text}')

    input('Press Enter to start')
    startTime = round(time())
    txt = input('-> ')
    endTime = round(time())
    inputTime = (endTime - startTime)

    characters = len(txt)
    words = len(txt.split())

    cpm = round(characters/inputTime*60)
    wpm = round(words/inputTime*60)

    wrong = 0
    minLen = min(len(txt), len(text))
    for i in range(minLen):
        if txt[i] != text[i]:
            wrong += 1

    try:
        accuracy = 100 - round(wrong/minLen*100)
    except ZeroDivisionError:
        accuracy = 0

    return cpm, wpm, accuracy

def main():
    while True:
        func = cpm_wpm()
        end = f'\nYour cpm is {func[0]}\nyour wpm is {func[1]}\nyour accuracy is {func[2]}%\n'
        print(end)
        while True:
            more = input('''Would you like to play once more?
                            No, I won't (0)
                            Yes, sure   (1)
                            -> ''')
            if more in ('yes', 'sure', '1', 'yes, sure', 'yes, sure (1)', 'yes, sure   (1)', '(1)', 'no, I won\'t (0)', 'no', 'I won\'t', 'won\'t', 'wouldn\'t', '0', '(0)'):
                break
            else:
                print('Please, choice again')
        if more.lower() in ('yes', 'sure', '1', 'yes, sure', 'yes, sure (1)', 'yes, sure   (1)', '(1)'):
            print(end)
        elif more.lower() in ('no, I won\'t (0)', 'no', 'I won\'t', 'won\'t', 'wouldn\'t', '0', '(0)'):
            break

    print('Thank you for playing, goodbye!')
    sleep(0.25)

if __name__ == '__main__':
    main()
