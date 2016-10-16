# -*- coding: utf-8 -*-
import pygame
import pygame.midi
from pygame.locals import *
from giantwin32 import *
from relative_tempered_generator import nextNoteFrecuency, chord

pygame.init()

pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input(input_id)

pygame.display.set_caption("midi test")
screen = pygame.display.set_mode((400, 300), RESIZABLE, 32)

print("starting")

going = True

while going:

        events = event_get()
        for e in events:
                if e.type in [QUIT]:
                        going = False
                if e.type in [KEYDOWN]:
                        going = False

        if i.poll():
                midi_events = i.read(10)
                print(midi_events)
                if int(midi_events[0][0][0]) in [224, 225, 226]:
                    print(str(midi_events[0][0][2]))


print("exit button clicked.")
i.close()
pygame.midi.quit()
pygame.quit()
exit()