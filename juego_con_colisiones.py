import random
import arcade

SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_COIN = 0.3
GOOD_COUNT = random.randint(1, 50)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites")

        self.player_list = None
        self.good_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.HOOKER_GREEN)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/robot/robot_jump.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(GOOD_COUNT):

            good = arcade.Sprite(":resources:images/tiles/mushroomRed.png", SPRITE_SCALING_COIN)

            good.center_x = random.randrange(SCREEN_WIDTH)
            good.center_y = random.randrange(SCREEN_HEIGHT)

            self.good_list.append(good)

    def on_draw(self):
        arcade.start_render()
        self.good_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):

        self.good_list.update()

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.good_list)

        for good in good_hit_list:
            good.remove_from_sprite_lists()
            self.score += 1


def main():

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

