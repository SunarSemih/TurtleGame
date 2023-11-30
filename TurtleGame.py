import turtle
import random
import time

# Ekran oluşturma
turtleGame_board = turtle.Screen()
turtleGame_board.title("Kaplumbağa Tıklama Oyunu")
turtleGame_board.bgcolor("#D2B48C")  # RGB değeri ile kahverengi rengi
turtleGame_board.setup(width=600, height=600)

# Kaplumbağa oluşturma
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()
kaplumbaga.speed(0)

# Skor
score = 0

# Skor tablosunu oluştur
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("black")
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Geri sayım
time_limit = 30
time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.color("black")
time_display.goto(0, 230)
time_display.write("Time: {}".format(time_limit), align="center", font=("Courier", 18, "normal"))

# Fare tıklandığında gerçekleşecek olay
def tıklama_olayı(x, y):
    global score
    if kaplumbaga.distance(x, y) < 20:
        kaplumbaga.color("red")
        yeni_konum()
        score += 1
        update_score()

# Yeni konum belirleme
def yeni_konum():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    kaplumbaga.goto(x, y)
    kaplumbaga.color("green")

# Skoru güncelleme
def update_score():
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Geri sayım güncelleme
def update_time():
    global time_limit
    time_limit -= 1
    time_display.clear()
    time_display.write("Time: {}".format(time_limit), align="center", font=("Courier", 18, "normal"))

# Fare tıklanma olayını dinle
turtleGame_board.onclick(tıklama_olayı)

# Geri sayım başlatma
while time_limit > 0:
    update_time()
    time.sleep(1)

# Oyun bitti mesajı
score_display.clear()
score_display.goto(0, 0)
score_display.write("Game Over\nScore: {}".format(score), align="center", font=("Courier", 36, "normal"))

turtleGame_board.mainloop()
