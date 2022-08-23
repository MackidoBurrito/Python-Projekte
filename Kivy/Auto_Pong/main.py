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
            offset = (ball.center_y - self.center_y) / (self.height / 20)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.5
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

    def spawn_powerup(self, spawn):
        spawn.spawned = 0
        if spawn.spawned <= 0:
            spawn.spawned == 1
            print("PowerUP Spawned")


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

    def serve_ball(self, vel=(8, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def serve_items(self):
        w = random.uniform(200.0, Window.size[0] - 200.0)
        h = random.uniform(50.0, Window.size[1] - 50)
        self.spawn.center = [w, h]

    def update(self, dt):
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
            self.serve_ball(vel=(8, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-8, 0))

        # move pedals automatically
        randomnr = random.randrange(-75, 75)
        self.player1.center_y = self.ball.center_y + randomnr
        randomnr2 = random.randrange(-75, 75)
        self.player2.center_y = self.ball.center_y + randomnr2

        # automatic power ups spawn
        if random.randrange(0, 100) == 0:
            self.serve_items()


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
