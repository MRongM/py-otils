
import os
import time
from multiprocessing import Process

from otils.oo import _OO


class Worker(Process, _OO):
    def __init__(self, function, data, **kwargs):
        super(Worker, self).__init__()
        self.func = function
        self.data = data
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.filename = f'process_worker_{self.begin}_{self.end}_{int(time.time() * 100000)}'

    def run(self):
        ident = os.getpid()
        self.orun(ident)
