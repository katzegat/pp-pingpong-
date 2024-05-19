from pygame import *
from random import randint
init()

class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_width - 260:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 260:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window =display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

rocket1 = Player('rocket.png', 30, 200, 50, 150, 4)
rocket2 = Player('rocket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tennis ball.png', randint(150, 350), randint(150, 350), 50, 50, 4)

y_speed = 3
x_speed = 3

font.init()
font = font.Font(None, 36)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rocket1.update_l()
        rocket2.update_r()

        ball.rect.x += x_speed
        ball.rect.y += y_speed

        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            x_speed *= -1
        
        if ball.rect.y <0 or ball.rect.y >win_height - 50:
            y_speed *= -1
        
        if ball.rect.x <0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
        rocket1.reset()
        rocket2.reset()
        ball.reset()
    else:
        finish = False
        time.delay(10000)
        window.fill(back)
        rocket1.rect.y = 200
        rocket2.rect.y = 200
        ball.rect.y = randint(150, 350)
        ball.rect.x = randint(150, 350)
    display.update()
    clock.tick(FPS)