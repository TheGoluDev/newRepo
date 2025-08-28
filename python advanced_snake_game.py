"""
Advanced Snake Game (Pygame)

Features:
- Smooth grid-based movement
- Increasing speed as score increases
- Score + persistent high score (saved in highscore.txt)
- Pause (P), Restart (R), Quit (Q/ESC)
- Game Over screen with options
- Arrow keys + WASD controls
- Food never spawns on snake

Requirements:
- Python 3.8+
- pygame (pip install pygame)

Run:
python advanced_snake_game.py
"""

import pygame
import sys
import random
import os
from collections import deque

# ---------- Config ----------
CELL_SIZE = 20
GRID_WIDTH = 32
GRID_HEIGHT = 24
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS_BASE = 8
FPS_INCREMENT_EVERY = 3
FPS_INCREMENT = 1

SNAKE_COLOR = (10, 180, 10)
SNAKE_HEAD_COLOR = (0, 120, 0)
FOOD_COLOR = (200, 30, 30)
BG_COLOR = (15, 15, 20)
GRID_COLOR = (30, 30, 40)
TEXT_COLOR = (230, 230, 230)

HIGH_SCORE_FILE = "highscore.txt"

# ---------- Utilities ----------
def load_high_score(path=HIGH_SCORE_FILE):
    try:
        with open(path, "r") as f:
            return int(f.read().strip() or 0)
    except Exception:
        return 0

def save_high_score(score, path=HIGH_SCORE_FILE):
    try:
        with open(path, "w") as f:
            f.write(str(score))
    except Exception:
        pass

# ---------- Game Objects ----------
class Snake:
    def __init__(self, start_pos, length=4):
        # build snake body facing right
        x, y = start_pos
        self.body = deque([(x - i, y) for i in range(length)])
        self.direction = (1, 0)  # moving right
        self.grow_by = 0

    def head(self):
        return self.body[0]

    def move(self):
        hx, hy = self.head()
        dx, dy = self.direction
        new = ((hx + dx) % GRID_WIDTH, (hy + dy) % GRID_HEIGHT)  # wrap-around
        self.body.appendleft(new)
        if self.grow_by > 0:
            self.grow_by -= 1
        else:
            self.body.pop()

    def change_direction(self, new_dir):
        dx, dy = new_dir
        cdx, cdy = self.direction
        if (dx == -cdx and dy == -cdy) and len(self.body) > 1:
            return  # ignore reverse
        self.direction = new_dir

    def grow(self, amount=1):
        self.grow_by += amount

    def collides_with_self(self):
        return self.head() in list(self.body)[1:]

    def occupies(self, pos):
        return pos in self.body

class Food:
    def __init__(self, pos):
        self.pos = pos

# ---------- Game Logic ----------
class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Advanced Snake - Pygame")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 28)
        self.large_font = pygame.font.SysFont(None, 64)

        self.high_score = load_high_score()
        self.reset()

    def reset(self):
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = Snake((start_x, start_y))
        self.spawn_food()
        self.score = 0
        self.game_over = False
        self.paused = False
        self.fps = FPS_BASE

    def spawn_food(self):
        while True:
            pos = (random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT))
            if not self.snake.occupies(pos):
                self.food = Food(pos)
                return

    def handle_key(self, key):
        if key in (pygame.K_UP, pygame.K_w):
            self.snake.change_direction((0, -1))
        elif key in (pygame.K_DOWN, pygame.K_s):
            self.snake.change_direction((0, 1))
        elif key in (pygame.K_LEFT, pygame.K_a):
            self.snake.change_direction((-1, 0))
        elif key in (pygame.K_RIGHT, pygame.K_d):
            self.snake.change_direction((1, 0))
        elif key == pygame.K_p:
            self.paused = not self.paused
        elif key == pygame.K_r:
            self.reset()
        elif key in (pygame.K_ESCAPE, pygame.K_q):
            pygame.quit()
            sys.exit()

    def update(self):
        if self.game_over or self.paused:
            return

        self.snake.move()

        # collision with self
        if self.snake.collides_with_self():
            self.game_over = True
            if self.score > self.high_score:
                self.high_score = self.score
                save_high_score(self.high_score)
            return

        # ate food
        if self.snake.head() == self.food.pos:
            self.score += 1
            self.snake.grow(1)
            self.spawn_food()
            if self.score % FPS_INCREMENT_EVERY == 0:
                self.fps += FPS_INCREMENT

    def draw(self):
        self.screen.fill(BG_COLOR)

        # food
        fx, fy = self.food.pos
        pygame.draw.rect(self.screen, FOOD_COLOR, (fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # snake
        for i, (x, y) in enumerate(self.snake.body):
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = SNAKE_HEAD_COLOR if i == 0 else SNAKE_COLOR
            pygame.draw.rect(self.screen, color, rect)

        # score + high score
        score_surf = self.font.render(f"Score: {self.score}", True, TEXT_COLOR)
        hs_surf = self.font.render(f"High Score: {self.high_score}", True, TEXT_COLOR)
        self.screen.blit(score_surf, (8, 8))
        self.screen.blit(hs_surf, (8, 8 + score_surf.get_height() + 4))

        if self.paused:
            self.draw_center_text("PAUSED", self.large_font)

        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    def draw_center_text(self, text, font, y_offset=0):
        surf = font.render(text, True, TEXT_COLOR)
        rect = surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
        self.screen.blit(surf, rect)

    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        self.draw_center_text("GAME OVER", self.large_font, -60)
        lines = [
            f"Score: {self.score}",
            f"High Score: {self.high_score}",
            "Press R to Restart, Q/ESC to Quit",
        ]
        for i, l in enumerate(lines):
            self.draw_center_text(l, self.font, -10 + i * 28)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)

            self.update()
            self.draw()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    SnakeGame().run()
