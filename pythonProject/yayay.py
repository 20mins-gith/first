import pygame
import random
import sys
import math
import os


# Set up the display
WIDTH = 800
HEIGHT = 600

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (148, 0, 211)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")
playerhealth = 10000
superbulletamount = 100


class Enemies:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def shoot(self, targetx, targety):
        for i in range(30):
            bullet = Bullet(self.x, self.y, player.x + random.randint(i, 100),
                            player.y + random.randint(i, 100), False, 10, 5)
            enemybullets.append(bullet)


class Enemythree(Enemies):

    def draw(self, surface):
        pygame.draw.circle(surface, BLACK, (self.x, self.y), self.radius)

    def shoot(self, targetx, targety):
        bullet2 = Bullet(self.x, self.y, targetx, targety, False, 3, 10)
        enemybullets.append(bullet2)


class Enemytwo(Enemies):

    def draw(self, surface):
        pygame.draw.circle(surface, PURPLE, (self.x, self.y), self.radius)

    def shoot(self, targetx, targety):
        for i in range(5):
            bullet2 = Bullet(self.x, self.y, self.x, self.y + 1, False, 10 + 3 * i, 5)
            enemybullets.append(bullet2)


class Enemy(Enemies):
    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, self.y), self.radius)


class Player:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 5

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed


class Bullet:
    def __init__(self, x, y, target_x, target_y, type, speed, size):
        self.type = type
        self.x = x
        self.y = y
        self.speed = speed
        angle = math.atan2(target_y - y, target_x - x)
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)
        self.size = size

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.type == True:
            for e in enemies[:]:
                if math.hypot(bullet.x - e.x, bullet.y - e.y) < e.radius:
                    bullets.remove(self)
                    enemies.remove(e)
                    break

    def draw(self, surface):
        pygame.draw.circle(surface, BLACK, (int(self.x), int(self.y)), self.size)

    def is_off_screen(self):
        return self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT


class SuperBullet(Bullet):

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), 5)


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


# Create a player
player = Player(WIDTH // 2, HEIGHT // 2, 20)
enemies = []
bullets = []
superbullets = []
enemybullets = []
# Game loop
clock = pygame.time.Clock()
running = True
state = 0

while running:
    if state == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Start the game when Enter is pressed
                    state = 1
                    # Initialize game objects (player, enemies, bullets)
                    player = Player(WIDTH // 2, HEIGHT // 2, 20)
                    enemies = []
                    bullets = []
                    superbullets = []
                    enemybullets = []
                    playerhealth = 10 # Reset health

        screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        sprite_image2 = pygame.image.load(os.path.join("Good starting screen (no epilepsy)2.png")).convert_alpha()
        screen.blit(sprite_image2, (0, 0 ))


        # Update the display
        pygame.display.flip()
        # Cap the frame rate
        clock.tick(60)

    if state == 2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Start the game when Enter is pressed
                    state = 1
                      # Initialize game objects (player, enemies, bullets)
                    player = Player(WIDTH // 2, HEIGHT // 2, 20)
                    enemies = []
                    bullets = []
                    superbullets = []
                    enemybullets = []
                    playerhealth = 100  # Reset health

        screen.fill(BLACK)
        sprite_image3 = pygame.image.load(os.path.join("Good END screen (no epilepsy).png")).convert_alpha()
        screen.blit(sprite_image3, (0, 0))

            # Update the display
        pygame.display.flip()
            # Cap the frame rate
        clock.tick(60)


    if state == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in range(30):
                        bullet = Bullet(player.x, player.y, mouse_x + random.randint(i, 100,),
                                        mouse_y + random.randint(i, 100), False, 10, 5)
                        bullets.append(bullet)
                if event.button == 4 or event.button == 5 or event.button == 3:  # Right mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    superbullet = SuperBullet(player.x, player.y, mouse_x, mouse_y, False, 5, 5)
                    superbullets.append(superbullet)
                    superbulletamount -= 1


        # Handle continuous key presses
        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] + keys[pygame.K_d] - keys[pygame.K_a])
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP] + keys[pygame.K_s] - keys[pygame.K_w])

        if random.randint(1, 30) == 1:
            new_x = random.randint(0, WIDTH)
            new_y = 0
            new_radius = 20
            speed = 1
            new_enemy = Enemy(new_x, new_y, new_radius, speed)
            enemies.append(Enemy(random.randint(0, WIDTH), 0, 20, 1))
            enemies.append(Enemytwo(random.randint(0, WIDTH), 0, 17.5, 2))
            enemies.append(Enemythree(random.randint(0, WIDTH), 0, 30, 0.5))

        for enemy in enemies:
            if random.randint(1, 250) == 1:
                enemy.shoot(player.x, player.y)

        player.move(dx, dy)

        # Move and remove off-screen enemies
        for e in enemies:
            e.move(0, 1)  # Move downwards
            if e.y > HEIGHT + e.radius:
                enemies.remove(e)

        # Update bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                bullets.remove(bullet)
            else:
                for e in enemies[:]:
                    if math.hypot(bullet.x - e.x, bullet.y - e.y) < e.radius:
                        bullets.remove(bullet)
                        enemies.remove(e)
                        break

                        # Check for collision with enemies
        for sb in superbullets[:]:
            sb.update()
            if sb.is_off_screen():
                superbullets.remove(sb)
            else:
                for e in enemies[:]:
                    if math.hypot(sb.x - e.x, sb.y - e.y) < e.radius:
                        enemies.remove(e)
                        break
                # Check for collision with enemies

        for bullet in enemybullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                enemybullets.remove(bullet)
            else:
                # Check for collision with enemies
                e = player
                if math.hypot(bullet.x - e.x, bullet.y - e.y) < e.radius:
                    enemybullets.remove(bullet)
                    playerhealth -= 1



        # Clear the screen
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        draw_text(f"health: {playerhealth}", font, RED, WIDTH // 4 - 150, HEIGHT // 2 + 250)
        draw_text(f"superbullets: {superbulletamount}", font, RED, WIDTH // 4 - 150, HEIGHT // 2 + 200)
        if superbulletamount <= 0:
            draw_text("No more superbullets", font, RED, WIDTH // 4 - 150, HEIGHT // 2 + 175)

        # Draw the player, enemies, and bullets
        player.draw(screen)
        for e in enemies:
            e.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for sb in superbullets:
            sb.draw(screen)
        for enemybullet in enemybullets:
            enemybullet.draw(screen)

        if playerhealth <= 0:
            state = 2




        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()