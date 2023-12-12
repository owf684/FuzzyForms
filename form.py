import pygame
from button import Button
from label import Label
class Form:
    def __init__(self,x,y,w,h):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x,y,w,h)
        self.back_rect = pygame.Rect(x-4,y-4,w+8,h+8)

        self.color = (60,60,60)
        self.back_color = (150,150,150)
        self.buttons = {}
        self.labels = {}
        self.combo_boxes = {}
        self.entry_boxes = {}





    def update(self,screen):
        pygame.draw.rect(screen,self.back_color,self.back_rect)
        pygame.draw.rect(screen,self.color,self.rect)
        
        for key, button in self.buttons.items():
            button.update(screen)

        for key, label in self.labels.items():
            label.update(screen)

    def add_button(self,button_name,x,y,w,h):
        button_x = x + self.x
        button_y = y + self.y
        if button_x+w > self.x + self.w \
            or x < 0:

            button_x = self.x
       

        if button_y+h > self.y + self.h \
            or y < 0:

            button_y = self.y


        self.buttons[button_name] = Button(button_x,button_y,w,h)

    def add_label(self,label_name,text,x,y,font_size):
        
        label_x = x + self.x
        label_y = y + self.y
        if label_x> self.x + self.w or x < 0:

            label_x = self.x
       

        if label_y > self.y + self.h  or y < 0:

            label_y = self.y
        self.labels[label_name] = Label(text,label_x,label_y,font_size)

