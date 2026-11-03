import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Aceita?')
root.geometry('600x600')
root.configure(background = '#ffb6c1')

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        "Meu amor", '❤️Meu amor, Sete anos se passaram desde o dia em que olhei nos seus olhos e disse “sim” para a melhor decisão da minha vida. E hoje, olhando para trás, percebo que cada dia vivido ao seu lado foi um presente. Nesses sete anos, aprendemos a rir juntos das pequenas coisas, a atravessar as dificuldades de mãos dadas e a comemorar cada conquista como se fosse a primeira. Você me viu nos meus melhores dias e me abraçou nos piores, e foi assim que entendi que o amor de verdade não está só nos grandes momentos, mas nos gestos simples do cotidiano: no café feito com carinho, no olhar cúmplice, no silêncio confortável de quem se sente em casa. Dizem que o sétimo ano é um marco, e para mim ele é a prova de que escolher você, todos os dias, nunca foi um esforço, sempre foi uma alegria. Você é meu porto seguro, meu melhor amigo, meu maior apoio e o meu lugar favorito no mundo. Obrigado(a) por cada memória construída, por cada sonho compartilhado e por todo o amor que você me dá sem pedir nada em troca. Eu me apaixono por você de novo a cada manhã. Que venham mais sete, e depois mais sete, e todos os anos que a vida nos permitir. Porque, onde você estiver, é ali que está o meu coração. Feliz sete anos de casamento. Eu te amo, hoje e sempre. Com todo o meu amor❤️')


def denied():
    button_1.destroy()


margin = Canvas(root, width=500, bg='#ffb6c1', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = Label(root, bg='#ffb6c1', text='Quer namorar comigo?',
                fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()

button_1 = tk.Button(root, text='Não', bg='#ffb6c1', command=denied,
                     relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.place(x=300, y=250)

root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='Sim', bg='#ffb6c1', relief=RIDGE,
                     bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.pack()

root.mainloop()