#!/usr/bin/env python3
import pyxel


class App(object):
    def __init__(self):
        self.initialize_variables()
        pyxel.init(250, 120, caption="mario_run")
        pyxel.image(0).load(0, 0, "mario.png")
        pyxel.image(1).load(0, 0, "cribo.png")
        pyxel.image(2).load(0, 0, "kupa.png")

        # self.music_play()
        pyxel.run(self.update, self.draw)

    def initialize_variables(self):
        self.mario_x, self.mario_y = 0, 90
        self.mario_dx, self.mario_dy = 3, 5
        self.mario_dt, self.fly_standard = 0, 50
        self.mario_state, self.cribo_state = "normal", "left"
        self.kupa_x, self.kupa_y = 200, 90
        self.cribo_x, self.cribo_y = 120, 90

        self.score = 0

    def music_play(self):
        pyxel.sound(0).set(
            "c2re2rg2rc3c3 c3c3b2a2g2f2e2d2",
            "p",
            "6",
            "n",
            20,
        )
        pyxel.sound(1).set(
            "c2re-2rg2rc3c3 c3c3b2c3d3c3b2d3",
            "p",
            "6",
            "nnnnnnnn nnnnnnnn",
            20,
        )
        pyxel.play(0, [0, 1], loop=True)

    def update(self):
        self.mario_x = (self.mario_x + 1) % pyxel.width
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.mario_state = "jump"

        self.object_movemant()
        self.mario_movement()
        self.score = self.score + 1

    def mario_movement(self):
        if(self.mario_state == "jump"):
            self.mario_y = self.mario_y - self.mario_dy
            self.mario_x = self.mario_x + self.mario_dx
            if(self.mario_y < self.fly_standard):
                self.mario_y = 90
                self.mario_state = "normal"

        if(self.cribo_x+4 <= self.mario_x <= self.cribo_x+10 and
           self.mario_y == self.cribo_y):
            self.score = self.score - 100

        if(self.kupa_x+4 <= self.mario_x <= self.kupa_x+10 and
           self.mario_y == self.kupa_y):
            print("GAMW OVER!! your core is " + str(self.score))
            pyxel.quit()

    def object_movemant(self):
        if(self.cribo_x <= 0):
            self.cribo_state = "right"
        elif(self.cribo_x > pyxel.width-16):
            self.cribo_state = "left"

        if(self.cribo_state == "left"):
            self.cribo_x = (self.cribo_x - 1) % pyxel.width
        elif(self.cribo_state == "right"):
            self.cribo_x = (self.cribo_x + 1) % pyxel.width

        self.kupa_x = (self.kupa_x - 1) % pyxel.width

    def draw(self):
        pyxel.cls(1)
        pyxel.blt(self.mario_x, self.mario_y, 0, 0, 0, 16, 16, 0)
        pyxel.blt(self.cribo_x, self.cribo_y, 1, 0, 0, 16, 16, 0)
        pyxel.blt(self.kupa_x, self.kupa_y, 2, 0, 0, 16, 16, 0)
        pyxel.text(100, 5, "Dodge, object!", pyxel.frame_count % 10)
        pyxel.text(20, 5, str(self.score)+"km", 4)


App()
