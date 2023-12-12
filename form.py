import pygame
from button import Button
from label import Label
from entry import Entry
from combo_box import ComboBox


class Form:
    def __init__(self, x, y, w, h):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.back_rect = pygame.Rect(x - 4, y - 4, w + 8, h + 8)
        self.render = False
        self.color = (60, 60, 60)
        self.back_color = (40, 40, 40)
        self.buttons = {}
        self.labels = {}
        self.combo_boxes = {}
        self.entries = {}

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
            combo_box.update(screen)

    def add_button(self, button_name, text, x, y, w, h):
        button_x = x + self.x
        button_y = y + self.y
        if button_x + w > self.x + self.w \
                or x < 0:
            button_x = self.x

        if button_y + h > self.y + self.h \
                or y < 0:
            button_y = self.y

        self.buttons[button_name] = Button(text, button_x, button_y, w, h)

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
        self.entries[entry_name] = Entry(x+self.x, y+self.y, w, h, font_size)

    def add_combo_box(self, combo_box_name, x, y, w, h):

        self.combo_boxes[combo_box_name] = ComboBox(x+self.x, y+self.y, w, h)
