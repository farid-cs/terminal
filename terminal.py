#!/bin/env python3

import pyray as rl

import os
import pty
import subprocess

WINDOW_TITLE = 'terminal'
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1200

def start_terminal():
    pid, fd = pty.fork()

    if pid == 0:
        subprocess.run(['printf', 'Hello from child process!'])
        return

    message = os.read(fd, 1024)

    rl.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    while not rl.window_should_close():
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)
        rl.draw_text(message.decode(), 0, 0, 30, rl.BLACK)

        rl.end_drawing()

if __name__ == '__main__':
    start_terminal()
