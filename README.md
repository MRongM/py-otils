### [py-otils](https://github.com/MRongM/py-otils.git)
- 

### 说明
- python office tools for human beings
- 常用工具包装模块

### 安装
```
python setup.py install
```

### 示例

#### 线程并行

```python
from otils import Manager

tm = Manager(lambda x: x + 10, list(range(10)), num=2, test=True)
tm.do_work()

```

#### 进程并行

- windows下进程执行入口必须为**if \_\_name\_\_ == '\_\_main\_\_':**
- handler function **不支持lambda**

```python
from otils import Manager

def foo(x):
    return x + 10

def Process_test():
    tm = Manager(foo, list(range(10)), num=2, wtype='process')
    tm.do_work()

if __name__ == '__main__':
    Process_test()

```

#### 处理函数
- 处理函数支持单函数传递，也支持函数列表
- 对于需要特殊参数的函数可以通过闭包或者偏函数来解决；将参数封装到item内，由处理函数解包处理也是一种办法

- 偏函数
```python
from functools import partial

def add(m, n):
    return m+n

def Thread_partial_test():
    add_100 = partial(add,100)
    add_10 = partial(add, 10)

    func_list = [add_10, add_100]
    tm = Manager(func_list, list(range(11)), num=2, test=True)
    tm.do_work()

```

- 闭包
- windows下多进程需要序列化，闭包不支持序列化，所以windows多进程闭包不支持
```python
def wadd(x):
    def add(m):
        return m+x
    return add

def Thread_closure_test():
    add_100 = wadd(100)
    add_10 = wadd(10)

    func_list = [add_10, add_100]
    tm = Manager(func_list, list(range(11)), num=2, test=True)
    tm.do_work()

```

#### 其他工具

- 文本与xlsx读写

```python
from otils import Writer,Reader
wr = Writer('id',suffix='txt',delimiter=',')
data = [['1','2','3'],['4','5','6']]
wr.write(data)

wr = Writer('id',suffix='xlsx')
data = [['1','2','3'],['4','5','6']]
wr.write(data)

rd = Reader('id',suffix='txt',delimiter=',')
rd.read()
```

- 时间函数

```python
from otils import now_add,now

now_add(7)
now()
```

- 文件大小

```python
from otils import get_size
get_size(path)

```

