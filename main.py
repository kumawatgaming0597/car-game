import pygame
import random
import sys
from car import Car
from obstacle import Obstacle

# Pygame initialize
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

class CarGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("🚗 Car Racing Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        
        # Game variables
        self.score = 0
        self.level = 1
        self.speed = 5
        self.font = pygame.font.Font(None, 36)
        
        # Initialize player car
        self.car = Car(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT - 100)
        
        # Obstacles
        self.obstacles = []
        self.spawn_rate = 0
        
    def spawn_obstacle(self):
        """Obstacles spawn करो"""
        x = random.randint(50, SCREEN_WIDTH - 50)
        obstacle = Obstacle(x, -50)
        self.obstacles.append(obstacle)
    
    def handle_events(self):
        """Events को handle करो"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
    
    def handle_input(self):
        """Keyboard input handle करो"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.car.move_left()
        if keys[pygame.K_RIGHT]:
            self.car.move_right()
        if keys[pygame.K_UP]:
            self.car.move_up()
        if keys[pygame.K_DOWN]:
            self.car.move_down()
    
    def update(self):
        """Game logic update करो"""
        if self.paused:
            return
        
        self.handle_input()
        
        # Obstacles spawn करो
        self.spawn_rate += 1
        if self.spawn_rate > 30 - (self.level * 2):
            self.spawn_obstacle()
            self.spawn_rate = 0
        
        # Obstacles को update करो
        for obstacle in self.obstacles[:]:
            obstacle.update(self.speed)
            
            # Screen से बाहर निकले तो remove करो
            if obstacle.rect.top > SCREEN_HEIGHT:
                self.obstacles.remove(obstacle)
                self.score += 10
            
            # Collision check करो
            if self.car.rect.colliderect(obstacle.rect):
                print(f"Game Over! Score: {self.score}, Level: {self.level}")
                self.running = False
        
        # Level बढ़ाओ
        if self.score % 100 == 0 and self.score > 0:
            self.level = (self.score // 100) + 1
            self.speed = 5 + (self.level - 1)
    
    def draw(self):
        """Screen पर सब कुछ draw करो"""
        self.screen.fill(BLACK)
        
        # Draw road
        pygame.draw.rect(self.screen, (50, 50, 50), (40, 0, SCREEN_WIDTH - 80, SCREEN_HEIGHT))
        
        # Draw lane lines
        for y in range(0, SCREEN_HEIGHT, 40):
            pygame.draw.line(self.screen, YELLOW, (SCREEN_WIDTH // 2, y), (SCREEN_WIDTH // 2, y + 20), 2)
        
        # Draw car
        self.car.draw(self.screen)
        
        # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        
        # Draw score and level
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level}", True, GREEN)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))
        
        # Draw pause message
        if self.paused:
            pause_text = self.font.render("PAUSED", True, RED)
            self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2))
        
        pygame.display.flip()
    
    def run(self):
        """Game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = CarGame()
    game.run()