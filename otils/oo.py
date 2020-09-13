import time
import os


"""
一些对象
Writer
Reader
"""


class _OO:
    def orun(self, ident):
        ll = len(self.data)
        wres = []
        try:
            for idx in range(ll):
                if idx < self.begin or idx >= self.end:
                    continue
                item = self.data[idx]
                res = self.func(item)
                if res:
                    if self.test:
                        print(f'ident:{ident} num:{idx} item:{item} res:{res}')
                    wres.append([str(ident), str(idx), str(item), str(res)])
                if self.sleep:
                    time.sleep(self.sleep)
        except Exception as ee:
            print(f"ident:{ident} index:{idx} item:{self.data[idx]} error {ee}")
            print(f"exit orun and save to {self.filename}")
            raise ee
        finally:
            wr = Writer(self.filename, path=self.path, suffix=self.suffix)
            wr.write(wres)


class HandleUnit:
    """
    处理单元
    """
    def __init__(self, **kwargs):
        """
        只支持键值对传值 key=value
        """
        for k, v in kwargs.items():
            setattr(self, k, v)

    def handle(self):
        """
        处理方法，子对象需要实现此方法，用作处理函数
        """
        pass


class Writer:
    def __init__(self, filename, suffix='txt', delimiter='#', path=''):
        self.suffix = suffix
        self.delimiter = delimiter
        self.path = os.path.join(path, f'{filename}.{suffix}')

    def write(self, data):
        if self.suffix == 'xlsx':
            from xlsxwriter import workbook
            wb = workbook.Workbook(self.path)
            ws = wb.add_worksheet()

            for row, item in enumerate(data):
                for col, dat in enumerate(item):
                    ws.write(row, col, dat)
            wb.close()

        elif self.suffix == 'txt':
            ff = open(self.path, 'w', encoding='utf8')

            for item in data:
                line = self.delimiter.join(item)
                ff.write(line + '\n')

            ff.close()


class Reader:
    def __init__(self, filename, suffix='txt', delimiter='#', path=''):
        self.suffix = suffix
        self.delimiter = delimiter
        self.path = os.path.join(path, f'{filename}.{suffix}')

    def read(self):
        data = []

        if self.suffix == 'txt':
            ff = open(self.path, 'r', encoding='utf8')
            for i in ff.readlines():
                da = i.strip()
                if da:
                    data.append(da.split(self.delimiter))
            ff.close()

        return data


