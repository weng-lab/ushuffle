#!/usr/bin/env python

from __future__ import print_function
from subprocess import PIPE, Popen
import os, sys, re

def joinhere(*args):
    return os.path.realpath(os.path.join(os.path.dirname(__file__), *args))

class ushuffle(object):

    def __init__(self, s, k=2, seed=12345, cap=True):
        self._ushuf = joinhere("ushuffle")
        if cap:
            self._s = s.upper()
        else:
            self._s = s
        self._k = k
        self._seed = seed

    def shuffle(self):
        x= Popen([self._ushuf, "-s", self._s, "-n", "1", "-k", "%d" % self._k,
                     "-seed", "%d" % self._seed], stdout=PIPE).communicate()[0].decode("utf-8").rstrip()
        return x

if __name__ == "__main__":
    pass
