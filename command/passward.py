#!/usr/local/bin/python3.7
import string
import secrets
import os
from perl import getopts

home = os.environ["HOME"]
path = home + "/pass"
opt = getopts("n:l:")

if(opt.l):
    length = opt.l
else:
    length = 8

if (opt.n):
    name = opt.n
else:
    name = "passward"


def pass_gen(size):  # pass generate
    chars = string.ascii_uppercase + \
        string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(chars) for x in range(size))


text = (pass_gen(int(length)))
f = open(path, "a")
f.write(text + "\t" + name)
f.write("\n")
f.close
