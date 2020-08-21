from otils import Manager,cost
from functools import partial


def add(m, n):
    return m + n


def Thread_test():
    tm = Manager(lambda x: x + 10, list(range(11)), num=2, test=True,suffix='xlsx')
    tm.do_work()


def Thread_partial_test():
    add_100 = partial(add, 100)
    add_10 = partial(add, 10)

    func_list = [add_10, add_100]
    tm = Manager(func_list, list(range(11)), num=2, test=True)
    tm.do_work()


def foo(x):
    return x + 10


def Process_test():
    tm = Manager(foo, list(range(10)), num=2, wtype='process')
    tm.do_work()


def wadd(x):
    def add(m):
        return m + x

    return add


def Thread_closure_test():
    add_100 = wadd(100)
    add_10 = wadd(10)

    func_list = [add_10, add_100]
    tm = Manager(func_list, list(range(11)), num=2, test=True)
    tm.do_work()


def bar(x):
    if x > 2:
        raise RuntimeError(f'stop {x}')
    return x + 20


def Thread_error_test(test=True):
    func_list = [bar, foo]
    tm = Manager(func_list, list(range(11)), num=2, test=test)
    tm.do_work()

@cost()
def Coro_test(timeout=10):
    add_100 = wadd(100)
    add_10 = wadd(10)
    func_list = [add_10, add_100]
    tm = Manager(func_list, list(range(11)), num=3, test=True, wtype='coro',sleep=2,timeout=timeout)
    tm.do_work()


if __name__ == '__main__':
    # Thread_test()
    Coro_test()
    # Thread_partial_test()
    # Thread_closure_test()
    # Process_test()
    # Thread_error_test()
    print()
