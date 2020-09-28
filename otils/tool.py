import datetime
from datetime import timedelta
from functools import wraps
import time, os

"""
日常小工具
"""


def now_add(n=0, fmt='%Y-%m-%d'):
    now = datetime.datetime.now()
    add_data = now + timedelta(days=n)
    return add_data.strftime(fmt)


def now(fmt='%Y-%m-%d %H:%M:%S'):
    now = datetime.datetime.now()
    return now.strftime(fmt)


def get_size(path):
    """
    :param path: 文件路径 
    :return: size, size_kb, size_mb, size_gb
    """
    size = os.path.getsize(path)
    size_kb = size / 1024
    size_mb = size_kb / 1024
    size_gb = size_mb / 1024
    return size, size_kb, size_mb, size_gb


def batch_run_func(model, spec=None, no=None, test=False):
    """
    批量执行模块内空参数方法
    :param model: module
    :param spec: 指定执行某个模块方法
    :param no: 不执行某些方法 list or tuple
    :param test: 是否打印执行结果
    :return: 返回执行结果
    """
    ser = []
    import inspect
    from types import FunctionType
    attrs = dir(model)
    for ar in attrs:
        func = getattr(model, ar)
        if callable(func) and isinstance(func, FunctionType):
            fname = func.__name__
            ag = inspect.getargs(func.__code__)
            args = ag.args
            varargs = ag.varargs
            varkw = ag.varkw
            if args or varargs or varkw:
                continue
            if spec and type(spec) is str and fname == spec:
                ser.append(func)
                break
            if no and fname in no:
                continue
            if test:
                print(f'batch start {fname}')
            res = func()
            if test:
                print(f'batch end {fname}')
            ser.append(res)
    print(model.__name__ + " done")
    return ser


def get_between(word, start, end):
    """
    匹配两个字符之间的任何字符串
    :param word: 被匹配字符串
    :param start: 开始字符串
    :param end: 结束字符串
    :return: str
    """
    import re
    return re.findall(f'{start}([\s\S]*){end}', word)


def cost(sli=None):
    """
    函数执行时间
    :param sli int or tuple or list 切片args以打印
    """

    if sli is None:
        sli = (0, 256)

    def _cost(func):
        @wraps(func)
        def warp(*args, **kwargs):
            st = time.time()
            rs = func(*args, **kwargs)
            if type(sli) is int:
                sargs = args[sli]
            else:
                sargs = args[sli[0]:sli[1]]
            print(
                f'pid:{os.getpid()} func name:{func.__name__} '
                f'cost:{time.time() - st} args:{sargs}' +
                (f"kwargs:{kwargs}" if kwargs else '')
            )
            return rs

        return warp

    return _cost

def run_server(python='python',port=8064):
    import subprocess
    import os
    server_path = os.path.join(os.path.split(os.path.realpath(__file__))[0],'server.py')
    print(server_path)
    p = subprocess.Popen([python, os.path.expanduser(server_path),port])
    print("server pid:",p.pid)