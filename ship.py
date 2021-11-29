import pygame
from laser import Laser


class Ship:
    COOLDOWN = 30;
    
    def __init__(self,x,y,window,health=100) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.surface = window
    
    
    
    def draw(self):
        self.surface.blit(self.ship_img,(self.x,self.y))
        for laser in self.lasers:
            laser.draw(self.surface)
        
    
    def move_lasers(self,vel,obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(750):
                self.lasers.remove(laser)
            
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
    
        
    @property
    def get_width(self):
        return self.ship_img.get_width()
    
    
    @property
    def get_height(self):
        return self.ship_img.get_height()

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter +=1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    
    def healthbar(self):
        pygame.draw.rect(self.surface,(255,0,0),(self.x,self.y+ self.ship_img.get_height()+10,self.ship_img.get_width(),10))
        pygame.draw.rect(self.surface,(0,255,0),(self.x,self.y+ self.ship_img.get_height()+10,self.ship_img.get_width() * (1-(self.max_health-self.health)/self.max_health),10))
    
    
   









