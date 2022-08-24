import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.context_instructions import Rotate


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 16)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.2
            if vel.x <= -50:
                vel.x = -50
            if vel.x >= 50:
                vel.x = 50
            if vel.y <= -100:
                vel.y = -100
            if vel.y >= 100:
                vel.y = 100
            ball.velocity = vel.x, vel.y + offset


class PowerUp(Widget):
    spawn = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pos = (-1000, -1000)


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    angle = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    spawn = ObjectProperty(None)
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    PowerUp_variation = 0
    spawned = False
    item_in_use = False
    old_window_size = (Window.size[0], Window.size[1])
    itemcooldown = random.randrange(180, 1000)

    def serve_ball(self, vel=(8, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    # spawn items
    def serve_items(self):
        self.PowerUp_variation = random.randrange(0, 2)
        w = random.uniform(200.0, Window.size[0] - 200.0)
        h = random.uniform(50.0, Window.size[1] - 50)
        if self.PowerUp_variation == 0:
            self.spawn.color = (20 / 255, 1, 0, 1)
            self.spawn.center = [w, h]
        else:
            self.spawn.color = (160 / 255, 0, 0, 1)
            self.spawn.center = [w, h]
        self.spawned = True

    def update_ball(self):
        self.ball.move()

        # rotation
        self.ball.angle += 5
        instructs = self.ball.canvas.children
        for instruct in instructs:
            if isinstance(instruct, Rotate):
                instruct.angle = self.ball.angle

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            if random.random() > 0.5:
                self.ball.velocity_y *= -1
            else:
                self.ball.y = self.height - self.ball.y - self.ball.height

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.player2.size = (51, 200)
            self.player2.size = (51, 200)
            self.serve_ball(vel=(8, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.player1.size = (51, 200)
            self.player2.size = (51, 200)
            self.serve_ball(vel=(-8, 0))

    def update_players(self):
        # move pedals automatically
        randrange_p1_1 = (self.player1.size[1] / 2 - 10) * -1
        randrange_p1_2 = self.player1.size[1] / 2 - 10
        randomnr = random.randrange(randrange_p1_1, randrange_p1_2)
        self.player1.center_y = self.ball.center_y + randomnr
        randrange_p2_1 = (self.player2.size[1] / 2 - 10) * -1
        randrange_p2_2 = self.player2.size[1] / 2 - 10
        randomnr2 = random.randrange(randrange_p2_1, randrange_p2_2)
        self.player2.center_y = self.ball.center_y + randomnr2

    def update_item(self, item):
        # automatic power ups spawn
        if self.itemcooldown == 0 and not self.spawned:
            self.serve_items()
        if self.itemcooldown > 0:
            self.itemcooldown -= 1
        # check if item has been collected
        if self.PowerUp_variation == 0:
            if self.ball.collide_widget(item):
                item.pos = (-1000, -1000)
                self.item_in_use = True
                self.spawned = False
                if self.ball.velocity_x > 0:
                    self.player1.size = (51, 300)
                else:
                    self.player2.size = (51, 300)
                self.itemcooldown = random.randrange(180, 1000)
        else:
            if self.ball.collide_widget(item):
                item.pos = (-1000, -1000)
                self.item_in_use = True
                self.spawned = False
                if self.ball.velocity_x > 0:
                    self.player1.size = (51, 50)
                else:
                    self.player2.size = (51, 50)
                self.itemcooldown = random.randrange(180, 1000)

        # check if window size is still correct
        if not (self.old_window_size[0] == Window.size[0]):
            if (self.old_window_size[1] == Window.size[1]):
                scale_x = Window.size[0] / self.old_window_size[0]
                scale_y = Window.size[1] / self.old_window_size[1]
                self.old_window_size = (Window.size[0], Window.size[1])
                new_x = self.spawn.center[0] * scale_x
                new_y = self.spawn.center[1] * scale_y
                self.spawn.center = [new_x, new_y]

        print(self.spawn.center)
        print(self.itemcooldown)
        print(self.PowerUp_variation)

    def update(self, dt):
        self.update_ball()
        self.update_players()
        self.update_item(self.spawn)


class PongApp(App):
    def build(self):
        game = PongGame()
        Window.fullscreen = 1
        Window.size = (1920, 1080)
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
