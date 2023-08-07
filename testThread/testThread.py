import random
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def down_load(file):
  start = time.time()
  print(file)
  print(f'开始下载{file}')
  time.sleep(random.randint(1,3))
  end = time.time()
  print(f'{file}下载完成，花费：{end - start:.3f}秒')

# def main():
#   start = time.time()
#   threads = [
#     Thread(target=down_load, args={'asf1.pdf'}),
#     Thread(target=down_load, args={'asf2.pdf'}),
#     Thread(target=down_load, args={'asf3.pdf'}),
#   ]
#   for thd in threads:
#     thd.start()
#   for thd in threads:
#     thd.join()
#   end = time.time()
#   print(f'总耗时{end - start:.3f}秒')

def main():
  with ThreadPoolExecutor(max_workers=4) as pool:
    start = time.time()
    files = ['asf1.pdf','asf2.pdf','asf3.pdf']
    for f in files:
      pool.submit(down_load, f)
  end = time.time()
  print(f'总耗时{end - start:.3f}秒')
  
main()