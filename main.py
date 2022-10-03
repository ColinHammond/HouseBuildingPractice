import arcade
my_window = arcade.open_window(800, 600, "Building a House")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
arcade.draw_rectangle_filled(300, 100, 200, 200, arcade.color.EGGSHELL)
arcade.draw_triangle_filled(200, 200, 300, 300, 400, 200, arcade.color.DEEP_CARMINE)
arcade.draw_rectangle_filled(300, 25, 50, 75, arcade.color.BROWN_NOSE)
arcade.draw_circle_filled(300, 150, 30, arcade.color.BLUEBERRY)
arcade.draw_circle_outline(300, 150, 30, arcade.color.BROWN_NOSE, 5)
arcade.draw_circle_filled(320, 25, 4, arcade.color.BRASS)

arcade.finish_render()
arcade.run()