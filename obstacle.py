import pygame

class Obstacle:
    """Obstacles class जो avoid करने हैं"""
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 60)
    
    def update(self, speed):
        """Obstacle को नीचे move करो"""
        self.rect.y += speed
    
    def draw(self, screen):
        """Obstacle को screen पर draw करो"""
        # Obstacle body (orange)
        pygame.draw.rect(screen, (255, 165, 0), self.rect)
        
        # Obstacle windows (dark)
        pygame.draw.rect(screen, (100, 100, 100), (self.rect.x + 5, self.rect.y + 10, 40, 15))
        
        # Obstacle headlights (white)
        pygame.draw.circle(screen, (255, 255, 255), (self.rect.x + 10, self.rect.y), 3)
        pygame.draw.circle(screen, (255, 255, 255), (self.rect.x + 40, self.rect.y), 3)
