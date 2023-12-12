import pygame
from form import Form

pygame.init()
clock = pygame.time.Clock()
running = True
screen_width = 680
screen_height = 480

new_form = Form(100, 100, 300, 300)
new_form.add_button('b1', 'OK', 50, 50, 50, 25)
new_form.add_label('l1', 'Hello, World', 300, 10, 12)
new_form.add_entry('e1', 200, 200, 100, 20, 18)
new_form.render = True

events = {'TextInput': None,
          'KeyDown': None}


def test():
    inputs = new_form.entries['e1'].get_text()
    new_form.labels['l1'].set_text(inputs)


screen = pygame.display.set_mode((screen_width, screen_height))
new_form.buttons['b1'].connect(test)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.TEXTINPUT:
            events['TextInput'] = event
        if event.type == pygame.KEYDOWN:
            events['KeyDown'] = event

    if new_form.render:
        new_form.update(screen, events)

    events['TextInput'] = None
    events['KeyDown'] = None

    pygame.display.flip()

    clock.tick(120) / 1000
