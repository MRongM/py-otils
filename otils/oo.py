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
        if type(self.handler) is type:
            flag = issubclass(self.handler, HandleUnit)
        else:
            flag = False
        try:
            for idx in range(ll):
                if idx < self.begin or idx >= self.end:
                    continue
                item = self.data[idx]

                try:
                    if flag:
                        """此时handler是类需要执行实例方法,入参为item"""
                        res = self.handler(item).handle()
                    else:
                        """此时handler是方法"""
                        res = self.handler(item)

                except Exception as ee:
                    print(f"ident:{ident} index:{idx} item:{self.data[idx]} error {ee}")
                    raise ee

                if self.test:
                    print(f'ident:{ident} num:{idx} item:{item} res:{res}')
                wres.append([str(ident), str(idx), str(item), str(res)])

                if self.sleep:
                    time.sleep(self.sleep)
        finally:
            if wres:
                wr = Writer(self.filename, path=self.path, suffix=self.suffix)
                wr.write(wres)


class HandleUnit:
    """
    处理单元
    """
    def handle(self):
        """
        处理方法，子对象需要实现此方法，用作处理函数
        """
        pass


class Writer:
    def __init__(self, filename, suffix='txt', delimiter='_#_', path='', title_translate=None):
        self.suffix = suffix
        self.delimiter = delimiter
        self.path = os.path.join(path, f'{filename}.{suffix}')
        self.title_translate = title_translate

    def _workbook_write(self, ws, data, is_dict=False):
        if is_dict:
            titles = data[0].keys()
            if self.title_translate:
                tran = [self.title_translate[i] for i in titles]
            else:
                tran = [titles]
            for item in data:
                row = []
                for title in titles:
                    row.append(item[title])
                tran.append(row)
            data = tran

        for row, item in enumerate(data):
            for col, dat in enumerate(item):
                ws.write(row, col, dat)

    def write(self, data):
        if self.suffix == 'xlsx':
            from xlsxwriter import workbook
            wb = workbook.Workbook(self.path)
            ws = wb.add_worksheet()
            self._workbook_write(ws, data, isinstance(data[0], dict))
            wb.close()

        elif self.suffix == 'txt':
            ff = open(self.path, 'w', encoding='utf8')

            for item in data:
                line = self.delimiter.join(item)
                ff.write(line + '\n')

            ff.close()


class Reader:
    def __init__(self, filename, suffix='txt', delimiter='_#_', path=''):
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


