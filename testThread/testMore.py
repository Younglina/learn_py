from concurrent.futures import ThreadPoolExecutor
from threading import RLock
import time

class Account:
    def __init__(self):
        self.blance = 0
        self.lock = RLock()
    
    def deposit(self, money):
        # self.lock.acquire()
        # try:
        #   count = self.blance + money
        #   time.sleep(0.1)
        #   self.blance = count
        # finally:
        #   self.lock.release()
        with self.lock:
          count = self.blance + money
          time.sleep(0.1)
          self.blance = count

def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=14) as pool:
        for _ in range(20):
            pool.submit(account.deposit, 1)
    print(account.blance)

main()
        