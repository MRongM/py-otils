from gevent import monkey, pool

monkey.patch_all()
import gevent

import time
from otils.oo import _OO
import os


class Worker(_OO):
    def __init__(self, function, data, **kwargs):
        super(Worker, self).__init__()
        self.func = function
        self.data = data
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.filename = f'coroutine_worker_{self.begin}_{self.end}_{int(time.time() * 100000)}'

    def run(self):
        ident = os.getpid()
        self.orun(ident)


def start(workers, num, timeout=None):
    po = pool.Pool(num)
    g = []
    for w in workers:
        g.append(po.spawn(w.run))
    gevent.joinall(g, timeout=timeout)
