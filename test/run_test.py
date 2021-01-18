from otils import batch_run_func

if __name__ == '__main__':
    module = __import__('manager_test')
    batch_run_func(module, test=True)
