import pygame
import time

# Initialisation de Pygame
pygame.init()

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Dimensions de l'écran
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Création de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tamagotchi")

# Classe Tamagotchi
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 100
        self.age = 0
        self.last_action_year = -1  # Année du dernier tour d'action
        self.is_alive = True

    def feed(self):
        if self.is_alive and self.age > self.last_action_year or self.last_action_year == 0:
            self.hunger -= 10
            self.happiness -= 5
            if self.hunger < 0:
                self.hunger = 0
            self.last_action_year = self.age
            self.age += 1
            if self.hunger >= 100 or self.happiness <= 0:
                self.is_alive = False
        elif not self.is_alive:
            print("Impossible de nourrir un Tamagotchi mort.")
        else:
            print("Une action par an, veuillez patienter.")

    def play(self):
        if self.is_alive and self.age > self.last_action_year:
            self.happiness += 10
            self.hunger += 5
            if self.happiness > 100:
                self.happiness = 100
            self.last_action_year = self.age
            self.age += 1
            if self.hunger >= 100 or self.happiness <= 0:
                self.is_alive = False
        elif not self.is_alive:
            print("Impossible de jouer avec un Tamagotchi mort.")
        else:
            print("Une action par an, veuillez patienter.")

    def time_passes(self):
        if self.is_alive and self.age > self.last_action_year:
            self.hunger += 5
            self.happiness -= 5
            self.last_action_year = self.age
            self.age += 1
            if self.hunger >= 100 or self.happiness <= 0:
                self.is_alive = False
        elif not self.is_alive:
            print("Le temps passe pour un Tamagotchi mort.")
        else:
            print("Une action par an, veuillez patienter.")

# Fonction pour afficher le Tamagotchi
def draw_tamagotchi(tamagotchi):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Nom: " + tamagotchi.name, True, BLACK)
    screen.blit(text, (10, 10))
    text = font.render("Faim: " + str(tamagotchi.hunger), True, BLACK)
    screen.blit(text, (10, 40))
    text = font.render("Bonheur: " + str(tamagotchi.happiness), True, BLACK)
    screen.blit(text, (10, 70))
    text = font.render("Age: " + str(tamagotchi.age), True, BLACK)
    screen.blit(text, (10, 100))
    if tamagotchi.is_alive:
        text = font.render("Il est en vie.", True, BLACK)
    else:
        text = font.render("Il est mort.", True, BLACK)
    screen.blit(text, (10, 130))

# Fonction pour dessiner un bouton
def draw_button(text, x, y, width, height, active):
    font = pygame.font.SysFont(None, 20)
    pygame.draw.rect(screen, GRAY if active else BLACK, (x, y, width, height))
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)
    screen.blit(text_surface, text_rect)

# Création du Tamagotchi
tamagotchi = Tamagotchi("Elina")

# Boucle principale du jeu
running = True
while running:
    screen.fill(WHITE)

    # Dessiner le Tamagotchi
    draw_tamagotchi(tamagotchi)

    # Dessiner les boutons
    draw_button("Nourrir (f)", 250, 10, 120, 30, tamagotchi.age > tamagotchi.last_action_year)
    draw_button("Jouer (p)", 250, 50, 120, 30, tamagotchi.age > tamagotchi.last_action_year)
    draw_button("Passer le temps (t)", 250, 90, 120, 30, True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 250 <= x <= 370 and 10 <= y <= 40:
                tamagotchi.feed()
            elif 250 <= x <= 370 and 50 <= y <= 80:
                tamagotchi.play()
            elif 250 <= x <= 370 and 90 <= y <= 120:
                tamagotchi.time_passes()

    pygame.display.flip()

    time.sleep(0.1)  # Attente courte pour limiter le taux de rafraîchissement de l'écran

pygame.quit()
