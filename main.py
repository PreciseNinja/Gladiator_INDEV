import pygame

# Entity Classes


class Mage:
    # Parameters
    def __init__(self, x, y, controls, team):
        self.x = x
        self.y = y
        self.img = pygame.image.load('mage.png')
        self.hitbox = self.img.get_rect()
        self.speed = 0.2
        self.controls = controls
        self.team = team

    #   Draw to screen(Modularized)
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    # Movement(Modularized)
    def move(self):
        if self.controls == 'wasd':
            keys = pygame.key.get_pressed()
            if self.team == 'blue':
                if keys[pygame.K_a] and self.controls == 'wasd':
                    self.img = pygame.image.load('mage2.png')
                    self.x -= self.speed
                    self.hitbox = self.img.get_rect()
                if keys[pygame.K_d] and self.controls == 'wasd':
                    self.img = pygame.image.load('mage.png')
                    self.x += self.speed
                    self.hitbox = self.img.get_rect()
                if keys[pygame.K_w] and self.controls == 'wasd':
                    self.y -= self.speed
                    self.hitbox = self.img.get_rect()
                if keys[pygame.K_s] and self.controls == 'wasd':
                    self.y += self.speed
                    self.hitbox = self.img.get_rect()
        if self.controls == 'arrow keys':
            keys = pygame.key.get_pressed()
            if self.team == 'red':
                if keys[pygame.K_LEFT]:
                    self.img = pygame.image.load('mage4.png')
                    self.x -= self.speed
                    self.hitbox = self.img.get_rect()
                if keys[pygame.K_RIGHT]:
                    self.img = pygame.image.load('mage3.png')
                    self.x += self.speed
                    self.hitbox = self.img.get_rect()
                if keys[pygame.K_UP]:
                    self.y -= self.speed
                    self.hitbox = self.img.get_rect()
                if keys[pygame.K_DOWN]:
                    self.y += self.speed
                    self.hitbox = self.img.get_rect()


class Horseman:
    def __init__(self, x, y, controls):
        self.x = x
        self.y = y
        self.img = pygame.image.load('Horseman.png')
        self.hitbox = self.img.get_rect()
        self.speed = 0.4
        self.controls = controls

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        if self.controls == 'wasd':
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.controls == 'wasd':
                self.img = pygame.image.load('Horseman.png')
                self.x -= self.speed
                self.hitbox = self.img.get_rect()
            if keys[pygame.K_d] and self.controls == 'wasd':
                self.img = pygame.image.load('Horseman2.png')
                self.x += self.speed
                self.hitbox = self.img.get_rect()
            if keys[pygame.K_w] and self.controls == 'wasd':
                self.y -= self.speed
                self.hitbox = self.img.get_rect()
            if keys[pygame.K_s] and self.controls == 'wasd':
                self.y += self.speed
                self.hitbox = self.img.get_rect()
            if keys[pygame.K_SPACE] and self.controls == 'wasd':
                pass
        if self.controls == 'arrow keys':
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.img = pygame.image.load('Horseman.png')
                self.x -= self.speed
                self.hitbox = self.img.get_rect()
            if keys[pygame.K_RIGHT]:
                self.img = pygame.image.load('Horseman2.png')
                self.x += self.speed
                self.hitbox = self.img.get_rect()
            if keys[pygame.K_UP]:
                self.y -= self.speed
                self.hitbox = self.img.get_rect()
            if keys[pygame.K_DOWN]:
                self.y += self.speed
                self.hitbox = self.img.get_rect()


# Redraws Window(And draws parameter passed to it, Modularized)
def redrawwindow(entity):
    entity.draw()
    entity.move()


classinput = input('P1: Choose a class(Available Options: Mage, Horseman) ')
if classinput == 'Mage':
    print("Player 1 is: Mage.  You'll move with wasd, and attack with space.  Use C for your ability!")
    p = Mage(50, 50, 'wasd', 'blue')
elif classinput == 'Horseman':
    print("Player 1 is: Horseman. You'll move with wasd, and attack with space.  Use C for your ability!")
    p = Horseman(50, 50, 'wasd')

classinput2 = input('P2: Choose a class(Available Options: Mage, Horseman) ')
if classinput2 == 'Mage':
    print("Player 2 is Mage.  You'll move with arrow keys and attack with shift.  Use / for your ability!")
    p2 = Mage(730, 530, 'arrow keys', 'red')
elif classinput2 == 'Horseman':
    print("Player 2 is Horseman.  You'll move with arrow keys and attack with shift.  Use / for your ability!")
    p2 = Horseman(730, 530, 'arrow keys')

pygame.init()
screen = pygame.display.set_mode((800, 600))


def main():
    running = True
    while running:
        if p.x > 730:
            p.x = 730
        if p.y > 530:
            p.y = 530
        if p.x < 0:
            p.x = 0
        if p.y < 0:
            p.y = 0
        if p2.x > 730:
            p2.x = 730
        if p2.y > 530:
            p2.y = 530
        if p2.x < 0:
            p2.x = 0
        if p2.y < 0:
            p2.y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        redrawwindow(p)
        redrawwindow(p2)
        pygame.display.update()
        screen.fill((0, 150, 0))


main()
