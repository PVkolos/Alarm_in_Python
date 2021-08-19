import pyglet
import time, sys
from tkinter import *

root = Tk()
root.geometry("420x450")
root.resizable(width=False, height=False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
cn = Canvas(root, bg='white', height=30, width=30)
canvas = Canvas(root, bg='white', height=screen_height, width=screen_width)
root.title('Будильник')


def start():
    try:
        text_houre = text_hour.get()
        text_minutese = text_minutes.get()
        timee = str(time.strftime("%H:%M:%S", time.localtime()))
        count = (int(text_hour.get()) - int(timee[:2])) * 60 + (int(text_minutes.get()) - int(timee[3:5]))
        if count > -1 and (int(text_houre) <= 23 and int(text_minutese) <= 59):
            mus = variable.get()
            l = Label(root, text=f'Будильник установлен на {text_hour.get()}:{text_minutes.get()}',
                                bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=43, height=2)
            l.place(x=0, y=340)
            l = Label(root, text=f'Будильник будет воспроизведен через {count} мин.',
                                bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=43, height=2)
            l.place(x=0, y=400)
            root.update()
            time.sleep(4)
            root.destroy()
            i = True
            while True:
                 timee = str(time.strftime("%H:%M:%S", time.localtime()))
                 if timee[:5] == f'{text_houre}:{text_minutese}' and i:
                     i = False
                     sound = pyglet.media.load(f'{mus}.mp3', streaming=True)
                     sound.play()
                     time.sleep(30)
                     sys.exit()
                 time.sleep(1)
        else:
            l = Label(root, text='Проверьте вводимые данные!',
                                bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=43, height=2)
            l.place(x=0, y=340)
    except:
        pass


lbl = Label(root, text=f'Текущее время: {str(time.strftime("%H:%M:%S", time.localtime()))[:5]}',
                    bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=80, height=2)
lbl2 = Label(root, text='Установить будильник на:',
                    bg='#DA692F', fg='#000000', bd=2, font='Verdana', width=26, height=1)
hour = Label(root, text='Введите час',
                    bg='#DA692F', fg='#000000', bd=2, font='Verdana', width=15, height=1)
minutes = Label(root, text='Введите минуту',
                    bg='#DA692F', fg='#000000', bd=2, font='Verdana', width=15, height=1)
text_hour = Entry(root, bg='#CECECE', font='Cambria', justify='center', width=5)
text_minutes = Entry(root, bg='#CECECE', font='Cambria', justify='center', width=5)
btn = Button(text="⏰ Установить будильник ⏰", width=35, height=2, bg='#6EA6C1',
                        fg='#000000', font=('Verdana', 13, 'bold'), command=start)

miusik = Label(root, text=f'Выберете мелодию:',
                    bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=20, height=2)
variable = StringVar(root)
shr = OptionMenu(root, variable, 'Мелодия 1', 'Мелодия 2', 'Мелодия 3', 'Мелодия 4', 'Мелодия 5')

lbl.pack()
lbl2.place(x=0, y=60)
hour.place(x=45, y=90)
minutes.place(x=45, y=130)
text_hour.place(x=210, y=91)
text_minutes.place(x=210, y=131)
miusik.place(x=10, y=190)
shr.place(x=240, y=190)
btn.place(x=0, y=270)
canvas.pack()
root.mainloop()
