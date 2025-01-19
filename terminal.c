#include <raylib.h>
#include <stdlib.h>

static const char WINDOW_NAME[] = "terminal"; 
static const int WINDOW_WIDTH = 1600;
static const int WINDOW_HEIGHT = 1200;

int
main(void)
{
	InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME);

	while (!WindowShouldClose()) {
		BeginDrawing();
		EndDrawing();
	}

	return EXIT_SUCCESS;
}
