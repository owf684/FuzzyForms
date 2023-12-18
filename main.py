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

new_form.add_combo_box('cb1', 50, 50, 100, 50)
for i in range(20):
    new_form.combo_boxes['cb1'].add_entry(str(i))


new_form.add_combo_box('cb2', 50, 100, 100, 50)
new_form.combo_boxes['cb2'].add_entry("Hello, World 1")
new_form.combo_boxes['cb2'].add_entry("Hello, World 2")
new_form.combo_boxes['cb2'].add_entry("Hello, world 3")

def on_change(**kwargs):
    name = kwargs['name']
    print(new_form.combo_boxes[name].selected_index, new_form.combo_boxes[name].index_offset)


new_form.combo_boxes['cb1'].connect(on_change, True)
new_form.combo_boxes['cb2'].connect(on_change, True)

new_form.render = True

events = {'TextInput': None,
          'KeyDown': None,
          'MouseWheel': None}

screen = pygame.display.set_mode((screen_width, screen_height))

while running:

    # clear screen
    screen.fill((0, 0, 0))

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
    events = {'TextInput': None,
              'KeyDown': None,
              'MouseWheel': None}
    pygame.display.flip()

    clock.tick(120) / 1000
