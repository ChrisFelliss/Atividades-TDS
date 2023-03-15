from tkinter import *
from tkinter import ttk


player = Tk()
player.title('Player')
player['bg'] = '#000000'
player.resizable(False, False)

width = int(650)
height = int(390)

screen_width = player.winfo_screenwidth()
screen_height = player.winfo_screenheight()

posx = screen_width/2 - width/2
posy = screen_height/2 - height/2 - screen_width *.033

print(screen_width, screen_height)
print(width, height)


player.geometry(f'{width}x{height}+{int(posx)}+{int(posy)}')

# Adicione a barra de progresso ao frame
style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", thickness=2, background='red')

f_width = width
f_heigth = 50

frame = Frame(player, width=f_width, height=f_heigth, bg='black')
frame.place(y=height-height*.10, x=0)

progress = ttk.Progressbar(frame, orient=HORIZONTAL, length=width-20, mode='determinate', style='TProgressbar')
progress.place(y=0, x=10)

playbutton = Button(frame, text='►', width=2, height=1, fg= 'white', bg='black', border=0)
playbutton.place(y=int(f_heigth*.18), x = 10)


def update_progress():
    value = progress["value"]
    if value < 100:
        progress["value"] = value + 0.01535
        player.after(1, update_progress)
    else:
        return

# inicia a atualização da barra de progresso
update_progress()

def interface():
    pass




player.mainloop()