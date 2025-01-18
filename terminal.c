#include <raylib.h>
#include <stdlib.h>

static const int WINDOW_WIDTH = 1600;
static const int WINDOW_HEIGHT = 1200;

int
main(void)
{
	InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "terminal");

	while (!WindowShouldClose()) {
		BeginDrawing();
		EndDrawing();
	}

	return EXIT_SUCCESS;
}
