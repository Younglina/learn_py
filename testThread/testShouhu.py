from threading import Thread
import time

def display(content):
  while(True):
    print(content, end='', flush=True)
    time.sleep(0.1)

def main():
  Thread(target=display, args={'ping'}, daemon=True).start()
  Thread(target=display, args={'pong'}, daemon=True).start()
  time.sleep(3)

main()