#!/bin/env python3

import pyray as rl

import errno
import os
import platform
import pty
import selectors
import subprocess
import sys
import time

WINDOW_TITLE = 'terminal'
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1200

def start_terminal():
    pid, fd = pty.fork()

    if pid == 0:
        # simulate work
        subprocess.run(['printf', 'Hello from child process!\n'])
        subprocess.run(['printf', 'How are you?\n'])
        subprocess.run(['printf', 'Bye!'])
        time.sleep(2)

        # cleanup
        os.close(sys.stdin.fileno())
        os.close(sys.stdout.fileno())
        os.close(sys.stderr.fileno())

        exit()

    sel = selectors.DefaultSelector()
    sel.register(fd, selectors.EVENT_READ)
    message = b''

    rl.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    while not rl.window_should_close():
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)
        rl.draw_text(message.decode().replace('\r', ''), 0, 0, 30, rl.BLACK)

        rl.end_drawing()

        try:
            if len(sel.select(0.1)) > 0:
                    message += os.read(fd, 1024)
        except OSError as err:
            if err.errno == errno.EIO and platform.system() == 'Linux':
                break
            raise err

    rl.close_window()

if __name__ == '__main__':
    start_terminal()
