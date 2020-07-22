### description
- python thread for human beings

### install
```
python setup.py install
```

### sample
```
from otils.HThread import TManager
tm = TManager(lambda x:x,list(range(100)),5)
tm.work()
```