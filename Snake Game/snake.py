from turtle import Turtle
INITIAL_POSITION = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.counter = 0

    # TODO Create snake
    def create_snake(self):
        """Create a three segment snake to start with"""
        for seg in INITIAL_POSITION:
            self.add_segment(seg)

    # TODO Add new segment to the snake
    def add_segment(self, position):
        # counter = 0
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        # new_segment.goto(i * -20, 0) #This code makes the snake generate 6 starting segment when create_snake in init
        new_segment.goto(position)
        self.segments.append(new_segment)
        # counter += 1
        # print(counter)
        # print(self.segments)

    # TODO Add segment when snake eats
    def extend(self):
        self.add_segment(self.segments[-1].position())


    # print(self.segments)
    # print(counter)

    # TODO Move the snake
    def move(self):
        """Move the following segment into the position of the current segment"""
        # self.counter += 1
        # print(self.counter)
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.move()
        # self.counter += 1
        # print(self.counter)