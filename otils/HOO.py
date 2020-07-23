import time
import os
import datetime
from datetime import timedelta
from xlsxwriter import workbook



"""
office utils for human beings

Writer
Reader

"""

class _OO:
    def orun(self, ident):
        ll = len(self.data)
        wres = []
        try:
            for idx in range(ll):
                item = self.data[idx]
                if idx < self.begin or idx >= self.end:
                    continue
                res = self.func(item)
                if res:
                    if self.test: print(f'ident:{ident} num:{idx} item:{item} res:{res}')
                    wres.append([str(ident), str(idx), str(item), str(res)])
                if self.sleep: time.sleep(self.sleep)
        finally:
            wr = Writer(self.filename, path=self.path, suffix=self.suffix)
            wr.write(wres)


class Writer:
    def __init__(self, filename, suffix='txt', delimiter='#', path=''):
        self.suffix = suffix
        self.delimiter = delimiter
        self.path = os.path.join(path, f'{filename}.{suffix}')

    def write(self, data):
        if self.suffix == 'xlsx':
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


