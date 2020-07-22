import threading
import time


class Worker(threading.Thread):

    def __init__(self, function, data, begin, end, sleep):
        super().__init__()
        self.__func = function
        self.data = data
        self.begin = begin
        self.end = end
        self.sleep = sleep
        self.filename = f'worker_{begin}_{end}_{int(time.time() * 100000)}.txt'

    def run(self) -> None:
        ident = threading.current_thread().ident
        ll = len(self.data)
        ff = open(self.filename, 'a', encoding='utf8')
        for idx in range(ll):
            item = self.data[idx]
            if idx < self.begin or idx >= self.end:
                continue
            res = self.__func(item)
            if res:
                ss = f'ident:{ident} num:{idx} item:{item} res:{res}'
                print(ss)
                ff.write(f'{ident}#{idx}#{item}#{res}\n')
            time.sleep(self.sleep)
        ff.close()


class TManager:
    def __init__(self, func, data, num=1, sleep=1, start=0, end=0, spec=False):
        self.func = func
        self.data = data
        self.workers = []
        if spec:
            wo = Worker(self.func, self.data, start, end, sleep)
            self.workers.append(wo)
        else:
            ll = len(self.data)
            cap = ll // num

            for i in range(0, ll, cap):
                wo = Worker(self.func, self.data, i, i+cap, sleep)
                self.workers.append(wo)

        print(f'assemble finished worker num:{len(self.workers)}')

    def work(self, join=True):

        for i in range(len(self.workers)):
            self.workers[i].start()
            print(f'worker {i} start')

        if join:
            for i in range(len(self.workers)):
                self.workers[i].join()
