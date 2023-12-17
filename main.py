import pygame
from form import Form

pygame.init()
clock = pygame.time.Clock()
running = True
screen_width = 800
screen_height = 600

new_form = Form(100,
                100,
                400,
                400)
new_form.add_entry('e1', 20, 200, 100, 25, 18)
new_form.add_button('b1', '->', 150, 200, 50, 25)
new_form.add_label('l1', 'Hello, World', 220, 200, 20)

new_form.add_entry('e2', 20, 50, 100, 25, 18)
new_form.add_button('b2', 'add entry', 150, 50, 100, 25)
new_form.add_combo_box('cb1', 275, 50, 100, 25)
new_form.add_switch('s1','sprite sheet',100,300,100,25)

new_form.render = True
i = 0
while i <= 20:
    new_form.combo_boxes['cb1'].add_entry(str(i))
    i+=1
events = {'TextInput': None,
          'KeyDown': None,
          'MouseWheel': None}


def test():
    inputs = new_form.entries['e1'].get_text()
    new_form.labels['l1'].set_text(inputs)


def add_entry():
    new_form.combo_boxes['cb1'].add_entry(new_form.entries['e2'].get_text())


screen = pygame.display.set_mode((screen_width, screen_height))
new_form.buttons['b1'].connect(test)
new_form.buttons['b2'].connect(add_entry)
while running:

    # clear screen
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.TEXTINPUT:
            events['TextInput'] = event
        if event.type == pygame.KEYDOWN:
            events['KeyDown'] = event
        if event.type == pygame.MOUSEWHEEL:
            events['MouseWheel'] = event

    if new_form.render:
        new_form.update(screen, events)

        # clear events dictionary
    events = {  'TextInput': None,
                'KeyDown': None,
                'MouseWheel': None}
    pygame.display.flip()

    clock.tick(120) / 1000
