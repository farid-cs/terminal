#include <raylib.h>
#include <stdlib.h>

static const char WINDOW_TITLE[] = "terminal";
static const int WINDOW_WIDTH = 1600;
static const int WINDOW_HEIGHT = 1200;

int
main(void)
{
	InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE);

	while (!WindowShouldClose()) {
		BeginDrawing();

		ClearBackground(RAYWHITE);
		DrawText("Hello World!", 0, 0, 30, BLACK);

		EndDrawing();
	}

	return EXIT_SUCCESS;
}
