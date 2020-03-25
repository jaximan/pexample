from time import sleep

from detailed import a, b


def something():
    sleep(1)
    a.something()
    b.something()
    print('This is C')


