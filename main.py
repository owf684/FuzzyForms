import pygame
from form import Form



def test():
    print('Hello, World!')

pygame.init()


running = True
screen_width = 680
screen_height = 480 

new_form = Form(100,100,300,300)
new_form.add_button('b1', 50, 50, 50, 25)
new_form.add_label('l1','Hello, World',300,10,12)

screen = pygame.display.set_mode((screen_width, screen_height))
new_form.buttons['b1'].connect(test)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        new_form.update(screen)


        pygame.display.flip()

