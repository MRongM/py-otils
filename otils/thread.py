import threading
from otils.oo import _OO
import time


class Worker(threading.Thread, _OO):

    def __init__(self, handler, data, **kwargs):
        super(Worker, self).__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.handler = handler
        self.data = data
        self.filename = f'thread_worker_{self.begin}_{self.end}_{int(time.time() * 100000)}'

    def run(self) -> None:
        ident = threading.current_thread().ident
        self.orun(ident)
