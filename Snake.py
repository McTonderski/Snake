#Snake by Kamil
#13 - 02 - 2019
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import random

window = Tk()
window.title('Snake')
window.geometry('310x300+150+150') #wymiary okna (wxh + position x + position y)
window.configure(background = 'dark green')


Width = 600 / 10
Height = 400 / 10
speed = 90
size = 10
pkt = 0

def game():
    window.destroy()
    window2 = Tk()
    window2.title('Snake')
    window2.geometry('+150+150')
    canvas = tk.Canvas(window2, width=600, height=400)
    canvas.configure(background='green')
    canvas.pack()

    class Area():
        def __init__(self):
            self.width = int(Width)
            self.height = int(Height)
            self.draw_wall()

        def draw_wall(self):
            for i in range(self.width):
                square(i * size, 0)
                square(i * size, (self.height - 1) * size)
            for i in range(1, self.height):
                square(0, i * size)
                square((self.width - 1) * size, i * size)

    class square():
        def __init__(self, x, y, color='dark green'):
            self.x = x
            self.y = y
            canvas.create_rectangle(self.x, self.y, self.x + size, self.y + size, fill=color)

    class Snake():
        def __init__(self):
            self.width = 60
            self.height = 40
            self.pkt = 0
            self.body = [[self.width / 2, self.height / 2], [self.width / 2 + 1, self.height / 2],
                         [self.width / 2 + 2, self.height / 2]]  # elementy (wektory poczatkowe) snake'a
            self.versor_move = [1 * size, 0]  # wektor poczatkowy do zmiany polozenia
            self.Food = [random.randint(1, self.width - 2) * size,
                         random.randint(1, self.height - 2) * size]  # wektor poczatkowy jedzenia
            self.col = False

        def DrawSnake(self):
            canvas.delete('all')
            if self.col:
                canvas.create_text([self.width / 2 * size, self.height / 2 * size],
                                   text=("Przegrałeś\nZdobyte punkty: ", pkt))
            else:
                for i in self.body:
                    square(i[0], i[1])  # rysowanie kwadracikow snake'a
                square((self.Food[0]), (self.Food[1]), color='red')
                Area()

        def move_snake(self):
            for i in range(len(self.body) - 1, 0, -1):  # podazanie elementow za pierwszym elementem
                self.body[i][0] = self.body[i - 1][0]
                self.body[i][1] = self.body[i - 1][1]

            self.body[0][0] += self.versor_move[0]  # dodawanie wektora poczatkowego do pierwszej pozycji snake'a
            self.body[0][1] += self.versor_move[1]
            self.colision()
            self.DrawSnake()
            self.eatFood()

        def eatFood(self):
            if self.body[0][0] == self.Food[0] and self.body[0][1] == self.Food[1]:
                self.body.append([0, 0])
                self.Food = [random.randint(1, self.width - 2) * size,
                             random.randint(1, self.height - 2) * size]  # nastepne polozenie jedzenia
                global pkt
                pkt += 1

        def colision(self):
            if self.body[0][0] == 0 or self.body[0][1] == 0 or self.body[0][0] == (self.width - 1) * size or \
                    self.body[0][1] == (self.height - 1) * size:
                self.col = True
            for i in self.body[1:]:
                if self.body[0][0] == i[0] and self.body[0][1] == i[1]:
                    self.col = True

        def reset(self):
            self.col = False
            global pkt
            pkt = 0
            self.Food = [random.randint(1, self.width - 2) * size,
                         random.randint(1, self.height - 2) * size]
            self.body = [[self.width / 2, self.height / 2], [self.width / 2 + 1, self.height / 2],
                         [self.width / 2 + 2, self.height / 2]]
            self.versor_move = [1 * size, 0]

        # zamiana wektora poczatkowego
        def moveRight(self):
            self.versor_move[0] = 1 * size
            self.versor_move[1] = 0

        def moveLeft(self):
            self.versor_move[0] = -1 * size
            self.versor_move[1] = 0

        def moveUp(self):
            self.versor_move[0] = 0
            self.versor_move[1] = -1 * size

        def moveDown(self):
            self.versor_move[0] = 0
            self.versor_move[1] = 1 * size

    def Game():
        area = Area()
        snake = Snake()

        def move():
            snake.move_snake()
            window2.after(speed, move) #aktualizuje obraz co 100ms

        def moveRight(event):
            snake.moveRight()

        def moveLeft(event):
            snake.moveLeft()

        def moveUp(event):
            snake.moveUp()

        def moveDown(event):
            snake.moveDown()

        window2.after(speed, move)
        window2.bind_all("<KeyPress-Left>", moveLeft)
        window2.bind_all("<KeyPress-Right>", moveRight)
        window2.bind_all("<KeyPress-Up>", moveUp)
        window2.bind_all("<KeyPress-Down>", moveDown)

        if snake.colision:
            Restart = Button(window2, text="Restart", command=snake.reset)
            Restart.pack()

    if __name__ == '__main__':
        Game()
    window2.mainloop()


def Easy():
    global speed
    speed = 100

def Normal():
    global speed
    speed = 60

def Hard():
    global speed
    speed = 20



text = Label(window, text = 'Snake', fg = 'Black', bg = 'dark green') #napis
text.config(font=("Courier", 100)) #czcionka i rozmiar
text.grid(row = 1,  columnspan = 3)

easy = Button(window, text = "Easy", command = Easy, width = 5, relief = RAISED)
easy.grid(row = 2, column = 0, pady = 20)

normal = Button(window, text = "Normal", command = Normal, width = 5)
normal.grid(row = 2, column = 1, pady = 20)

hard = Button(window, text = "Hard", command = Hard, width = 5)
hard.grid(row = 2, column = 2, pady = 20)

start = Button(window, text = "Start", command = game, width = 28)
start.grid(row = 3, columnspan = 3)


window.mainloop()

