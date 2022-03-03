import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")

    def on_draw(self):
        arcade.start_render()


def main():
    window = MyGame()
    arcade.run()


main()
