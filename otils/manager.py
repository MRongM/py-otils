from otils import thread
from otils import process
import os


class Manager:
    """
    任务并行分配器
    """

    def __init__(self, func, data_list, **kwargs):
        """
        :param func: 处理函数或者由处理函数组成的列表
        :param data_list: 数据集列表
        :param kwargs: 可选参数
        """
        if type(func) == list:
            self.func_list = func
        else:
            self.func_list = [func]
        self.data = data_list
        self.workers = []
        self.worker_init(**kwargs)

    def worker_init(self, num=None, sleep=None, begin=0, end=None, spec=False, wtype='thread', test=False, suffix='txt', path=''):
        """
        :param test: 执行任务是否打印
        :param wtype: 并行类型
        :param num: 并行数量
        :param sleep: 任务睡眠时间
        :param begin: 对data_list索引位置处理
        :param end: 对data_list索引位置处理
        :param spec: 是否对data_list索引位置处理
        :param wtype: 工作线程或者进程 thread or process
        :param path: 结果保存路径
        :param suffix: 文件后缀
        :return: None
        """
        self.wtype = wtype
        if self.wtype == 'thread':
            Worker = thread.Worker
        elif self.wtype == 'process':
            Worker = process.Worker
            num = num or os.cpu_count()
        else:
            raise ValueError('worker_type need specific')

        ll = len(self.data)

        if spec:
            end = end or ll
            kwarg = {
                'begin': begin,
                'end': end,
                'sleep': sleep,
                'test': test,
                'suffix': suffix,
            }
            wo = Worker(self.func_list[0], self.data, **kwarg)
            self.workers.append(wo)
        else:
            num = num or 1
            cap = ll // num
            idx = 0
            fl = len(self.func_list)
            for i in range(0, ll, cap):
                if idx >= fl:
                    func = self.func_list[-1]
                else:
                    func = self.func_list[idx]

                if idx + 1 == num:
                    to = ll
                else:
                    to = i + cap
                kwarg = {
                    'begin': i,
                    'end': to,
                    'sleep': sleep,
                    'test': test,
                    'suffix': suffix,
                    'path': path,
                }
                wo = Worker(func, self.data, **kwarg)
                self.workers.append(wo)

                if idx + 1 == num:
                    break
                idx += 1
        print(f'{self.wtype} assemble finished! worker num:{len(self.workers)}')

    def do_work(self, join=True):

        for i in range(len(self.workers)):
            self.workers[i].start()
            print(f'{self.wtype} worker {i} start')

        if join:
            for i in range(len(self.workers)):
                self.workers[i].join()
