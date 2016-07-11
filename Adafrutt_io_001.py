#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Jämföra två filer
#
import time
from Adafruit_IO import Client, Data
aio = Client('1326749aacca46de9b9b34c6a105cb92')


# Print out the feed names:
feeds = aio.feeds()
for f in feeds:
    print('Feed: {0}'.format(f.name))


# Print out the feed metadata.
feed = aio.feeds('StatusColor')
print(feed)

print '/n/n'
    

sc = aio.receive('StatusColor')
print sc
print sc.value

aio.send('StatusColor', '#ff0000')
time.sleep(2)
aio.send('StatusColor', '#ff8800')
time.sleep(2)
aio.send('StatusColor', '#ffff00')
time.sleep(2)
aio.send('StatusColor', '#00ff00')
