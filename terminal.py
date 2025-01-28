import pyray as rl

WINDOW_TITLE = 'terminal'
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1200

def main():
    rl.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    while not rl.window_should_close():
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)
        rl.draw_text('Hello World!', 0, 0, 30, rl.BLACK)

        rl.end_drawing()

if __name__ == '__main__':
    main()
