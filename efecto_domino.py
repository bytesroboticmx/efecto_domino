import pygame
import random

# Dimensiones de la ventana
width, height = 800, 600

# Clase para representar cada ficha de dominó
class DominoPiece:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        self.is_falling = False

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def fall(self):
        self.is_falling = True

    def is_offscreen(self):
        return self.rect.y >= height

pygame.init()

# Creación de la ventana de visualización
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Efecto dominó")
clock = pygame.time.Clock()

domino_pieces = []
piece_width = 40
piece_height = 80
gap = 5

# Creación de las fichas de dominó y colocación en la pantalla
for i in range(10):
    x = width // 2 - piece_width // 2
    y = i * (piece_height + gap)
    piece = DominoPiece(x, y, piece_width, piece_height)
    domino_pieces.append(piece)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Empujar la primera ficha para iniciar el efecto dominó
                domino_pieces[0].fall()

    screen.fill((255, 255, 255))

    for piece in domino_pieces:
        if piece.is_falling:
            piece.rect.y += 5

        piece.draw()

        if piece.is_offscreen():
            domino_pieces.remove(piece)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
