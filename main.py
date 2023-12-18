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

y_pos = 0
y_increment = 30

combo_dict =  {
    'cb1' : 'none',
    'cb2' : 'none',
    'cb3' : 'none',
    'cb4' : 'none'
}
for key, value in combo_dict.items():
    new_form.add_combo_box(key,20,y_pos,200,20)
    y_pos += y_increment
    for i in range(10):
        new_form.combo_boxes[key].add_entry(str(i))


new_form.render = True

events = {'TextInput': None,
          'KeyDown': None,
          'MouseWheel': None}




screen = pygame.display.set_mode((screen_width, screen_height))

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
