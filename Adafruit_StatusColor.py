#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Jämföra två filer
#
import time
from Adafruit_IO import Client, Data
aio = Client('1326749aacca46de9b9b34c6a105cb92')


while (True):
    status = raw_input('Choice color: (green, yellow, amber, red or x to exit)')
    if status[0] == 'g':
       color = '#00ff00'
    elif status[0] == 'y':
        color = '#ffff00'
    elif status[0] == 'a':
        color = '#ff6600'
    elif status[0] == 'r':
        color = '#ff0000'
    elif status[0] == 'x':
        break

    aio.send('StatusColor', color)
