
def now_add(n=0,fmt='%Y-%m-%d'):
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
    size_kb = size/1024
    size_mb = size_kb/1024
    size_gb = size_mb/1024
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
    attrs = dir(model)
    for ar in attrs:
        func = getattr(model, ar)
        if callable(func):
            fname = func.__name__
            ag = inspect.getargs(func.__doc__)
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
            res = func()
            if test: print(res)
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

