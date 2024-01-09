from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.c = 0
        self.initial_ps = (self.c, 0)
        self.body_seg = []
        self.create_body()
        self.head = self.body_seg[0]

    def create_body(self):
        for n in range(3):
            self.add_segment(position=self.initial_ps)
            self.c -= 20

    def add_segment(self, position):
        body = Turtle("circle")
        body.penup()
        body.color("blue")
        body.goto(position)
        self.body_seg.append(body)

    def extend(self):
        new_seg_pos = self.body_seg[-1].position()
        self.add_segment(new_seg_pos)

    def move(self):
        for n in range(len(self.body_seg) - 1, 0, -1):
            x = (self.body_seg[n - 1].xcor())
            y = (self.body_seg[n - 1].ycor())
            self.body_seg[n].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
