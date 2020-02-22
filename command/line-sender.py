#!/usr/bin/env python3
from linenotipy import Line
import subprocess
from subprocess import PIPE


class Bot(object):
    def __init__(self):
        self.line = Line(token="DVxKcN9dg0ecy9ETJtRpVHZr2Uouw1IyRDQtfxl3Ypk")

    def sender(self):
        self.line.post(message="finish experimt")
        self.stopper()

    def stopper(self):
        command = "sudo service cron start"
        proc = subprocess.Popen(
            command, shell=True, stderr=PIPE, stdout=PIPE, text=True)
        proc.communicate()[0]


def switch():
    command = "ps -aux | grep less | wc -l"
    proc = subprocess.Popen(
        command, shell=True, stderr=PIPE, stdout=PIPE, text=True)
    res = proc.communicate()
    return res[0].strip()


def main():
    sw = int(switch())
    bot = Bot()
    bot.sender() if sw == 2 else None


main()
