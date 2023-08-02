import time
from functools import wraps
def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间为：{end - start}')
        return result
    return wrapper

@record_time
def upload(filename):
    print(f'开始上传{filename}')
    time.sleep(2)
    print(f'{filename}下载完成')

upload('asdf.txt')

upload.__wrapped__('asdf2.txt')