# Импорт библиотек
from pygame import*
from random import*

# создание цвета
BLACK = (0, 0, 0)
LIGHT_BLUE = (80, 80, 255)
LIGHT_GREEN = (200, 255, 200)

# Инициализация шрифта и установка начальных переменных
font.init()
font = font.SysFont("arial", 30)
lost = 0  # Счетчик пропущенных яиц
score = 0  # Счетчик пойманных яиц
win_width = 700  # Ширина окна
win_height = 500  # Высота окна
coordinates = [90, 170, 250, 320, 400, 450, 500]  # Начальные координаты для яиц
clock = time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption("Мандаринолов")  # Заголовок окна

background = transform.scale(image.load("bgg.jpg"), (win_width, win_height))  # Загрузка фоновой картинки

# Создание класса для игровых спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Создание класса игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 100:
            self.rect.x += self.speed

# Создание класса для фруктов
class Eggs(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 450:
            lost += 1
            self.rect.y = 0
            self.rect.x = choice(coordinates)

wolf = Player("capybara_bobrova.png", 340, 340, 130, 130, 7)
eggs = sprite.Group()

for i in range(5):
    egg = Eggs("Mandarin.png", choice(coordinates), -80, 80, 80, randint(1, 5))
    eggs.add(egg)

# Основной цикл игры

run = True
while run:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    collision = sprite.spritecollide(wolf, eggs, True)
    for c in collision:
        print(c.image)
        Fruit = randint(1, 18)
            
        if Fruit == 1 or Fruit == 2 or Fruit == 3:
            egg = Eggs("Mandarin.png", choice(coordinates), -80, 80, 80, randint(1, 5))
            eggs.add(egg)
            score += 1
        elif Fruit == 4 or Fruit == 5 or Fruit == 6:
            egg = Eggs("Limon.png", choice(coordinates), -80, 80, 80, randint(1, 5))
            eggs.add(egg)
            score += 1

        elif Fruit == 7  or Fruit == 8  or Fruit == 9 :
            egg = Eggs("kavunchik.png", choice(coordinates), -80, 80, 80, randint(1, 5))
            eggs.add(egg)
            score += 1
            
        elif Fruit == 10  or Fruit == 11 or Fruit == 12 :
            egg = Eggs("mango.webp", choice(coordinates), -80, 80, 80, randint(1, 5))
            eggs.add(egg)
            score += 1
            
        elif Fruit == 13 or  Fruit == 14 or Fruit == 15:
            egg = Eggs("kumkvat.png", choice(coordinates), -80, 80, 80, randint(1, 5))
            eggs.add(egg)
            score += 1
            
        elif Fruit == 16 or Fruit == 17 or Fruit == 18:
            egg = Eggs("banan.png", choice(coordinates), -80, 80, 80, randint(1, 5))
            eggs.add(egg)
            score += 1

        
            
        
    # Отображение счета игрока
    text1 = font.render("Пропущено : " + str(lost), True, (255, 255, 255))
    window.blit(text1, (10, 60))
    text2 = font.render("Зловлено : " + str(score), True, (255, 255, 255))
    window.blit(text2, (10, 20))

    eggs.draw(window)
    eggs.update()

    wolf.reset()
    wolf.update()

    # Проверка условий победы и поражения
    if score >= 100:
        run = False
        win = transform.scale(image.load("POBEDA.jpg"), (win_width, win_height))
        text3 = font.render("капібара смачно наїлась фруктиків", True, (80, 0, 126))
        window.blit(win, (0, 0))
        window.blit(text3, (170, 215))
        display.update()
        time.wait(3000)

    if lost >= 3:
        run = False
        win = transform.scale(image.load("SADCAPYBARA.jpg"), (win_width, win_height))
        text4 = font.render("Ти зловив всього " + str(score) + " фруктів", True, (0, 0, 0))
        window.blit(win, (0, 0))
        window.blit(text4, (170, 215))
        display.update()
        time.wait(3000)

    clock.tick(60)
    display.update()
