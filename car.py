import pygame

class Car:
    """Player का car class"""
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.speed = 5
    
    def move_left(self):
        """Left में move करो"""
        if self.rect.left > 40:
            self.rect.x -= self.speed
    
    def move_right(self):
        """Right में move करो"""
        if self.rect.right < 360:
            self.rect.x += self.speed
    
    def move_up(self):
        """Up में move करो"""
        if self.rect.top > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        """Down में move करो"""
        if self.rect.bottom < 600:
            self.rect.y += self.speed
    
    def draw(self, screen):
        """Car को screen पर draw करो"""
        # Car body (red)
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        
        # Car windows (cyan)
        pygame.draw.rect(screen, (0, 255, 255), (self.rect.x + 5, self.rect.y + 10, 30, 15))
        
        # Car headlights (yellow)
        pygame.draw.circle(screen, (255, 255, 0), (self.rect.x + 10, self.rect.y), 3)
        pygame.draw.circle(screen, (255, 255, 0), (self.rect.x + 30, self.rect.y), 3)
