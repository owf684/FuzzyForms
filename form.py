import pygame
from button import Button
from label import Label
from entry import Entry
from combo_box import ComboBox
from switch import Switch

class Form:
    def __init__(self, x, y, w, h):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.back_rect = pygame.Rect(x - 1, y - 1, w + 2, h + 2)
        self.render = False
        self.color = (60, 60, 60)
        self.back_color = (40, 40, 40)
        self.buttons = {}
        self.labels = {}
        self.combo_boxes = {}
        self.entries = {}
        self.switches = {}
    def update(self, screen, events):
        pygame.draw.rect(screen, self.back_color, self.back_rect)
        pygame.draw.rect(screen, self.color, self.rect)

        for key, button in self.buttons.items():
            button.update(screen)

        for key, label in self.labels.items():
            label.update(screen)

        for key, entry in self.entries.items():
            entry.update(screen, events)

        for key, combo_box in self.combo_boxes.items():
            combo_box.update(screen, events)

        for key, switch in self.switches.items():
            switch.update(screen)

    def add_button(self, button_name, text, x, y, w, h):
        x_position, y_position = self.check_boundaries(x, y, w, h)
        self.buttons[button_name] = Button(text, x_position, y_position, w, h)

    def add_switch(self, switch_name, text, x, y, w, h):
        x_position, y_position = self.check_boundaries(x, y, w, h)
        self.switches[switch_name] = Switch(text, x_position, y_position, w, h)

    def add_label(self, label_name, text, x, y, font_size):

        label_x = x + self.x
        label_y = y + self.y

        self.labels[label_name] = Label(text, label_x, label_y, font_size)

        if label_x + self.labels[label_name].text_image.get_width() > self.x + self.w or x < 0:
            label_x = self.x

        if label_y + self.labels[label_name].text_image.get_height() > self.y + self.h or y < 0:
            label_y = self.y

        self.labels[label_name].rect = pygame.Rect(label_x, label_y, 0, 0)

    def add_entry(self, entry_name, x, y, w, h, font_size):
        x_position, y_position = self.check_boundaries(x, y, w, h)
        self.entries[entry_name] = Entry(x_position, y_position, w, h, font_size)

    def add_combo_box(self, combo_box_name, x, y, w, h):
        x_position, y_position = self.check_boundaries(x, y, w, h)
        self.combo_boxes[combo_box_name] = ComboBox(x_position, y_position, w, h)


    def check_boundaries(self, x, y, w, h):

        x_position = x + self.x

        if x_position + w > self.x + self.w:
            x_position = self.x + self.w - w
        elif x < 0:
            x_position = 0

        y_position = y + self.y

        if y_position + h > self.y + self.h:
            y_position = self.y + self.h - h
        if y < 0:
            y_position = 0

        return x_position, y_position
